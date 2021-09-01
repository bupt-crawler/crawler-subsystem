package handler

import (
	"errors"
	"github.com/gin-gonic/gin"
	"net/http"
	"strconv"
	"water_server/dal"
)

func GetDeviceHistoryOne(context *gin.Context) {
	offset, count, err := getOffsetAndCount(context)
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	var data []*dal.DeviceHistoryOne
	err = dal.MGetDeviceHistoryOneByDefault(&data, offset, count)
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error:": err.Error(),
		})
		return
	}

	context.JSON(http.StatusOK, data)
}

func GetDeviceHistoryTwo(context *gin.Context) {
	offset, count, err := getOffsetAndCount(context)
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	var data []*dal.DeviceHistoryTwo
	err = dal.MGetDeviceHistoryTwoByDefault(&data, offset, count)
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error:": err.Error(),
		})
		return
	}

	context.JSON(http.StatusOK, data)
}

func GetFlowAreaA(context *gin.Context) {
	offset, count, err := getOffsetAndCount(context)
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	var data []*dal.FlowAreaA
	err = dal.MGetFlowAreaAByDefault(&data, offset, count)
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	context.JSON(http.StatusOK, data)
}

func GetFlowAreaB(context *gin.Context) {
	offset, count, err := getOffsetAndCount(context)
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	var data []*dal.FlowAreaA
	err = dal.MGetFlowAreaBByDefault(&data, offset, count)
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	context.JSON(http.StatusOK, data)
}

func GetPortableDevice(context *gin.Context) {
	offset, count, err := getOffsetAndCount(context)
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	var data []*dal.FlowAreaA
	err = dal.MGetPortableDeviceByDefault(&data, offset, count)
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	context.JSON(http.StatusOK, data)
}

func GetSleet(context *gin.Context) {
	offset, count, err := getOffsetAndCount(context)
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	var data []*dal.Sleet
	err = dal.MGetSleetByDefault(&data, offset, count)
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	context.JSON(http.StatusOK, data)
}

func GetSystemErrorLog(context *gin.Context) {
	offset, count, err := getOffsetAndCount(context)
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	var data []*dal.SystemErrorLog
	err = dal.MGetSystemErrorLogByDefault(&data, offset, count)
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	context.JSON(http.StatusOK, data)
}

func GetDataErrorLog(context *gin.Context) {
	offset, count, err := getOffsetAndCount(context)
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	var data []*dal.DataErrorLog
	err = dal.MGetDataErrorLogByDefault(&data, offset, count)
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	context.JSON(http.StatusOK, data)
}

func getOffsetAndCount(context *gin.Context) (offset, count int, err error) {
	var countParam = context.Query("count")
	if len(countParam) == 0 {
		count = -1
	} else if count, err = strconv.Atoi(countParam); err != nil {
		count = -1
	}

	var offsetParam = context.Query("offset")
	if len(offsetParam) == 0 {
		offset = 0
	} else if offset, err = strconv.Atoi(offsetParam); err != nil {
		offset = 0
	}
	if count == -1 && offset != 0 {
		return offset, count, errors.New("invalid params")
	}

	return offset, count, nil
}
