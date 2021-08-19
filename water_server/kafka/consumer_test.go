package kafka

import (
	"github.com/Shopify/sarama"
	jsoniter "github.com/json-iterator/go"
	"testing"
	"water_server/consts"
	"water_server/dal"
)

func TestMain(m *testing.M) {
	m.Run()
}

//func TestConsumeSun(t *testing.T) {
//	partitionList, _ := Consumer.Partitions("sun")
//	for _, v := range partitionList {
//		t.Log(v)
//	}
//	for _, v := range partitionList {
//		partition, _ := Consumer.ConsumePartition("sun", int32(v), sarama.OffsetNewest)
//		defer partition.AsyncClose()
//		for msg := range partition.Messages() {
//			t.Log(string(msg.Value))
//		}
//	}
//}

func TestConsume(t *testing.T) {
	partitions, err := Consumer.Partitions(consts.PortableDevicePartition)
	if err != nil {
		t.Errorf("failed to get partition list, error: %v", err)
		return
	}
	pc, err := Consumer.ConsumePartition(consts.PortableDevicePartition, partitions[0], sarama.OffsetNewest)
	if err != nil {
		t.Errorf("failed to start consumer for partiton %s: %d, error: %v", consts.PortableDeviceTable, 0, err)
		return
	}
	defer Consumer.Close()
	defer pc.AsyncClose()
	for msg := range pc.Messages() {
		data := make(map[string]interface{})
		err := jsoniter.Unmarshal(msg.Value, &data)
		if err != nil {
			t.Errorf("failed to unmarshal message: %v", string(msg.Value))
			continue
		}
		err = dal.Insert(data, &dal.PortableDevice{})
		if err != nil {
			t.Errorf("failed to insert message: %v", data)
			continue
		}
	}
}
