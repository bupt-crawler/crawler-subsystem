package dal

import "time"

type DeviceHistoryOne struct {
	ID int `json:"id" gorm:"column:id"`
	Date time.Time `json:"date" gorm:"column:date"`
	SandMeasureID int `json:"sandMeasureId" gorm:"column:sandMeasureId"`
	GenFlowSpace float64 `json:"genFlowSpace" gorm:"column:genFlowSpace"`
	SandContent float64 `json:"sandContent" gorm:"column:sandContent"`
	DrySandLoss float64 `json:"drySandLoss" gorm:"column:drySandLoss"`
	Rainfall float64 `json:"rainfall" gorm:"column:rainfall"`
	RunoffWeight float64 `json:"runoffWeight" gorm:"column:runoffWeight"`
	RunoffDensity float64 `json:"runoffDensity" gorm:"column:runoffDensity"`
	DeviceV float64 `json:"deviceV" gorm:"column:deviceV"`
	ErrorCode int `json:"errorCode" gorm:"column:errorCode"`
}

type DeviceHistoryTwo struct {
	ID int `json:"id" gorm:"column:id"`
	Date time.Time `json:"date" gorm:"column:date"`
	SandMeasureID int `json:"sandMeasureId" gorm:"column:sandMeasureId"`
	GenFlowSpace float64 `json:"genFlowSpace" gorm:"column:genFlowSpace"`
	SandContent float64 `json:"sandContent" gorm:"column:sandContent"`
	DrySandLoss float64 `json:"drySandLoss" gorm:"column:drySandLoss"`
	Rainfall float64 `json:"rainfall" gorm:"column:rainfall"`
	RunoffWeight float64 `json:"runoffWeight" gorm:"column:runoffWeight"`
	RunoffDensity float64 `json:"runoffDensity" gorm:"column:runoffDensity"`
	DeviceV float64 `json:"deviceV" gorm:"column:deviceV"`
	ErrorCode int `json:"errorCode" gorm:"column:errorCode"`
}

type FlowAreaA struct {
	ID int `json:"id" gorm:"column:id"`
	Name string `json:"name" gorm:"column:name"`
	DeviceID int `json:"deviceId" gorm:"column:deviceId"`
	Date time.Time `json:"date" gorm:"column:date"`
	Time string  `json:"time" gorm:"column:time"`
	Flow float64 `json:"flow" gorm:"column:flow"`
	OneFlow float64 `json:"oneFlow" gorm:"column:oneFlow"`
	SandMeasure float64 `json:"sandMeasure" gorm:"column:sandMeasure"`
}

type FlowAreaB struct {
	ID int `json:"id" gorm:"column:id"`
	Name string `json:"name" gorm:"column:name"`
	DeviceID int `json:"deviceId" gorm:"column:deviceId"`
	Date time.Time `json:"date" gorm:"column:date"`
	Time string `json:"time" gorm:"column:time"`
	Flow float64 `json:"flow" gorm:"column:flow"`
	OneFlow float64 `json:"oneFlow" gorm:"column:oneFlow"`
	SandMeasure float64 `json:"sandMeasure" gorm:"column:sandMeasure"`
}

type PortableDevice struct {
	ID int `json:"id" gorm:"column:id"`
	Name string `json:"name" gorm:"column:name"`
	DeviceID int `json:"deviceId" gorm:"column:deviceId"`
	ProjectId int `json:"projectId" gorm:"column:projectId"`
	Date time.Time `json:"date" gorm:"column:date"`
	Longitude string `json:"longitude" gorm:"column:longitude"`
	Latitude string `json:"latitude" gorm:"column:latitude"`
	SandMeasure float64 `json:"sandMeasure" gorm:"column:sandMeasure"`
}

type Sleet struct {
	ID int `json:"id" gorm:"column:id"`
	Name string `json:"name" gorm:"column:name"`
	DeviceID int `json:"deviceId" gorm:"column:deviceId"`
	Date time.Time `json:"date" gorm:"column:date"`
	Longitude string `json:"longitude" gorm:"column:longitude"`
	Latitude string `json:"latitude" gorm:"column:latitude"`
	Temperature float64 `json:"temperature" gorm:"column:temperature"`
	Humidity float64 `json:"humidity" gorm:"column:humidity"`
	RainSnow float64 `json:"rainSnow" gorm:"column:rainSnow"`
	Duration float64 `json:"duration" gorm:"column:duration"`
}

type SystemErrorLog struct {
	ID int `json:"id" gorm:"column:id"`
	URL string `json:"url" gorm:"column:url"`
	Name string `json:"name" gorm:"column:name"`
	Time time.Time `json:"time" gorm:"column:time"`
	ErrorLog string `json:"errorLog" gorm:"column:errorLog"`
	AdditionalInfo string `json:"additionalInfo" gorm:"column:additionalInfo"`
}

type DataErrorLog struct {
	ID int `json:"id" gorm:"column:id"`
	DataInfo string `json:"dataInfo" gorm:"column:dataInfo"`
	ErrorLog string `json:"errorLog" gorm:"column:errorLog"`
	Time time.Time `json:"time" gorm:"column:time"`
	AdditionalInfo string `json:"additionalInfo" gorm:"column:additionalInfo"`
}
