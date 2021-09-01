package dal

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"gorm.io/gorm/schema"
	"water_server/consts"
)

var DB *gorm.DB

const (
	URL = "z217:zzhswdmz@tcp(120.53.104.59)/watermondb?charset=utf8&parseTime=True"
)

func init() {
	var err error
	DB, err = gorm.Open(mysql.Open(URL), &gorm.Config{NamingStrategy: schema.NamingStrategy{SingularTable: true}})
	if err != nil {
		panic("failed to connect database")
	}
}

func Insert(v interface{}, model interface{}) error {
	err := DB.Model(model).Create(v).Error
	return err
}

func mGet(data interface{}, condition map[string]interface{}, order string, table string, offset, count int) error {
	err := DB.Table(table).Where(condition).Offset(offset).Limit(count).Order(order).Find(data).Error
	return err
}

func getCount(model interface{}, condition map[string]interface{}) (int64, error) {
	var count int64
	err := DB.Model(model).Where(condition).Count(&count).Error
	if err != nil {
		return -1, err
	}
	return count, nil
}

func MGetDeviceHistoryOneByDefault(data interface{}, offset, count int) error {
	return mGet(data, map[string]interface{}{}, "date desc", consts.DeviceHistoryOneTable, offset, count)
}

func MGetDeviceHistoryTwoByDefault(data interface{}, offset, count int) error {
	return mGet(data, nil, "date desc", consts.DeviceHistoryTwoTable, offset, count)
}

func MGetFlowAreaAByDefault(data interface{}, offset, count int) error {
	return mGet(data, nil, "date desc, time desc", consts.FlowAreaATable, offset, count)
}

func MGetFlowAreaBByDefault(data interface{}, offset, count int) error {
	return mGet(data, nil, "date desc, time desc", consts.FlowAreaBTable, offset, count)
}

func MGetPortableDeviceByDefault(data interface{}, offset, count int) error {
	return mGet(data, nil, "date desc", consts.PortableDeviceTable, offset, count)
}

func MGetSleetByDefault(data interface{}, offset, count int) error {
	return mGet(data, nil, "date desc", consts.SleetTable, offset, count)
}

func MGetDataErrorLogByDefault(data interface{}, offset, count int) error {
	return mGet(data, nil, "time desc", consts.DataErrorLogTable, offset, count)
}

func MGetSystemErrorLogByDefault(data interface{}, offset, count int) error {
	return mGet(data, nil, "time desc", consts.SystemErrorLogTable, offset, count)
}

func GetDeviceHistoryOneCount() (int64, error) {
	return getCount(&DeviceHistoryOne{}, nil)
}

func GetDeviceHistoryTwoCount() (int64, error) {
	return getCount(&DeviceHistoryTwo{}, nil)
}

func GetFlowAreaACount() (int64, error) {
	return getCount(&FlowAreaA{}, nil)
}

func GetFlowAreaBCount() (int64, error) {
	return getCount(&FlowAreaB{}, nil)
}

func GetPortableDeviceCount() (int64, error) {
	return getCount(&PortableDevice{}, nil)
}

func GetSleetCount() (int64, error) {
	return getCount(&Sleet{}, nil)
}

func GetDataErrorLogCount() (int64, error) {
	return getCount(&DataErrorLog{}, nil)
}

func GetSystemErrorLogCount() (int64, error) {
	return getCount(&SystemErrorLog{}, nil)
}
