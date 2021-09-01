package kafka

import (
	"github.com/Shopify/sarama"
	jsoniter "github.com/json-iterator/go"
	"log"
	"strings"
	"time"
	"water_server/consts"
	"water_server/dal"
	"water_server/validation"
)

var (
	Consumer          sarama.Consumer
	partitionTableMap map[string]interface{}
	deviceHistoryOne  sarama.PartitionConsumer
	deviceHistoryTwo  sarama.PartitionConsumer
	flowAreaA         sarama.PartitionConsumer
	flowAreaB         sarama.PartitionConsumer
	portableDevice    sarama.PartitionConsumer
	sleet             sarama.PartitionConsumer
	systemErrorLog    sarama.PartitionConsumer
	dataErrorLog      sarama.PartitionConsumer
)

const (
	Host = "112.98.239.146"
	Port = "9092"
)

func init() {
	var err error
	Consumer, err = sarama.NewConsumer(strings.Split(Host+":"+Port, ","), nil)
	if err != nil {
		panic(err)
	}
	partitionTableMap = make(map[string]interface{})
	partitionTableMap[consts.FlowAreaAPartition] = &dal.FlowAreaA{}
	partitionTableMap[consts.FlowAreaBPartition] = &dal.FlowAreaB{}
	partitionTableMap[consts.PortableDevicePartition] = &dal.PortableDevice{}
	partitionTableMap[consts.SleetPartition] = &dal.Sleet{}
	go initConsumers()
}

func initConsumers() {
	var deviceHistoryOneChan, deviceHistoryTwoChan <-chan *sarama.ConsumerMessage
	var flowAreaAChan, flowAreaBChan <-chan *sarama.ConsumerMessage
	var portableDeviceChan, sleetChan <-chan *sarama.ConsumerMessage
	var systemErrorLogChan, dataErrorLogChan <-chan *sarama.ConsumerMessage
	var err error
	if err = initDeviceHistoryOne(); err == nil {
		defer func(deviceHistoryOne sarama.PartitionConsumer) {
			_ = deviceHistoryOne.Close()
		}(deviceHistoryOne)
		deviceHistoryOneChan = deviceHistoryOne.Messages()
	}
	if err = initDeviceHistoryTwo(); err == nil {
		defer func(deviceHistoryTwo sarama.PartitionConsumer) {
			_ = deviceHistoryTwo.Close()
		}(deviceHistoryTwo)
		deviceHistoryTwoChan = deviceHistoryTwo.Messages()
	}
	if err = initFlowAreaA(); err == nil {
		defer func(flowAreaA sarama.PartitionConsumer) {
			_ = flowAreaA.Close()
		}(flowAreaA)
		flowAreaAChan = flowAreaA.Messages()
	}
	if err = initFlowAreaB(); err == nil {
		defer func(flowAreaB sarama.PartitionConsumer) {
			_ = flowAreaB.Close()
		}(flowAreaB)
		flowAreaBChan = flowAreaB.Messages()
	}
	if err = initPortableDevice(); err == nil {
		defer func(portableDevice sarama.PartitionConsumer) {
			_ = portableDevice.Close()
		}(portableDevice)
		portableDeviceChan = portableDevice.Messages()
	}
	if err = initSleet(); err == nil {
		defer func(sleet sarama.PartitionConsumer) {
			_ = sleet.Close()
		}(sleet)
		sleetChan = sleet.Messages()
	}
	if err = initSystemErrorLog(); err == nil {
		defer func(systemErrorLog sarama.PartitionConsumer) {
			_ = systemErrorLog.Close()
		}(systemErrorLog)
		systemErrorLogChan = systemErrorLog.Messages()
	}
	if err = initDataErrorLog(); err == nil {
		defer func(dataErrorLog sarama.PartitionConsumer) {
			_ = dataErrorLog.Close()
		}(dataErrorLog)
		dataErrorLogChan = dataErrorLog.Messages()
	}

	var message *sarama.ConsumerMessage
	for {
		select {
		case message = <-deviceHistoryOneChan:
			_ = saveMessage(message.Value, &dal.DeviceHistoryOne{})
		case message = <-deviceHistoryTwoChan:
			_ = saveMessage(message.Value, &dal.DeviceHistoryTwo{})
		case message = <-flowAreaAChan:
			_ = saveMessage(message.Value, &dal.FlowAreaA{})
		case message = <-flowAreaBChan:
			_ = saveMessage(message.Value, &dal.FlowAreaB{})
		case message = <-portableDeviceChan:
			_ = saveMessage(message.Value, &dal.PortableDevice{})
		case message = <-sleetChan:
			_ = saveMessage(message.Value, &dal.Sleet{})
		case message = <-systemErrorLogChan:
			_ = saveMessage(message.Value, &dal.SystemErrorLog{})
		case message = <-dataErrorLogChan:
			_ = saveMessage(message.Value, &dal.DataErrorLog{})
		}
	}
}

func initDeviceHistoryOne() (err error) {
	deviceHistoryOne, err = Consumer.ConsumePartition(consts.DeviceHistoryOnePartition, 0, sarama.OffsetNewest)
	if err != nil {
		log.Printf("failed to consume partition: %s\n", consts.DeviceHistoryOnePartition)
		return
	}
	return
}

func initDeviceHistoryTwo() (err error) {
	deviceHistoryTwo, err = Consumer.ConsumePartition(consts.DeviceHistoryTwoTable, 0, sarama.OffsetNewest)
	if err != nil {
		log.Printf("failed to consume partition: %s\n", consts.DeviceHistoryTwoPartition)
		return
	}
	return
}

func initFlowAreaA() (err error) {
	flowAreaA, err = Consumer.ConsumePartition(consts.FlowAreaAPartition, 0, sarama.OffsetNewest)
	if err != nil {
		log.Printf("failed to consume partiton: %s\n", consts.FlowAreaAPartition)
		return
	}
	return
}

func initFlowAreaB() (err error) {
	flowAreaB, err = Consumer.ConsumePartition(consts.FlowAreaBPartition, 0, sarama.OffsetNewest)
	if err != nil {
		log.Printf("failed to consume partiton: %s\n", consts.FlowAreaBPartition)
		return
	}
	return
}

func initPortableDevice() (err error) {
	portableDevice, err = Consumer.ConsumePartition(consts.PortableDevicePartition, 0, sarama.OffsetNewest)
	if err != nil {
		log.Printf("failed to consume partition: %s\n", consts.PortableDevicePartition)
		return
	}
	return
}

func initSleet() (err error) {
	sleet, err = Consumer.ConsumePartition(consts.SleetPartition, 0, sarama.OffsetNewest)
	if err != nil {
		log.Printf("failed to consume partition: %s", consts.SleetPartition)
		return
	}
	return
}

func initSystemErrorLog() (err error) {
	systemErrorLog, err = Consumer.ConsumePartition(consts.SystemErrorLogPartition, 0, sarama.OffsetNewest)
	if err != nil {
		log.Printf("failed to consume partition: %s\n", consts.SystemErrorLogPartition)
		return
	}
	return
}

func initDataErrorLog() (err error) {
	dataErrorLog, err = Consumer.ConsumePartition(consts.DataErrorLogPartition, 0, sarama.OffsetNewest)
	if err != nil {
		log.Printf("failed to consume partition: %s\n", consts.DataErrorLogPartition)
		return
	}
	return
}

func saveMessage(message []byte, model interface{}) (err error) {
	data := make(map[string]interface{})
	err = jsoniter.Unmarshal(message, &data)
	// ensure no id
	delete(data, "id")
	if err != nil {
		log.Printf("failed to unmarshal message: %v\n", string(message))
		return
	}

	err = validation.NewMapValidation(data, model).Validate()
	if err != nil {
		errorLog := map[string]interface{}{
			"dataInfo": string(message),
			"errorLog": "params invalid",
			"time":     time.Now(),
		}
		_ = dal.Insert(errorLog, &dal.DataErrorLog{})
		return
	}

	err = dal.Insert(data, model)
	if err != nil {
		log.Printf("failed to insert data: %v\n", data)
		return
	}
	return
}
