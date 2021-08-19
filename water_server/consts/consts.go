package consts

import "time"

const (
	// Partition
	DeviceHistoryOnePartition = "device_history_one"
	DeviceHistoryTwoPartition = "device_history_two"
	FlowAreaAPartition        = "flow_area_a"
	FlowAreaBPartition        = "flow_area_b"
	PortableDevicePartition   = "portable_device"
	SleetPartition            = "sleet"
	SystemErrorLogPartition   = "system_error_log"
	DataErrorLogPartition     = "data_error_log"

	// Table
	DeviceHistoryOneTable = "device_history_one"
	DeviceHistoryTwoTable = "device_history_two"
	FlowAreaATable        = "flow_area_a"
	FlowAreaBTable        = "flow_area_b"
	PortableDeviceTable   = "portable_device"
	SleetTable            = "sleet"
	SystemErrorLogTable   = "system_error_log"
	DataErrorLogTable     = "data_error_log"

	PingInterval = 12 * time.Hour
)

var (
	URLs = map[string]string{
		"159.226.153.63": "西安三智",
		"gprs.sj2000.org": "北京天航佳德",
	}
)

