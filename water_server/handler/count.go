package handler

import (
	"github.com/gin-gonic/gin"
	"net/http"
	"water_server/dal"
)

func GetDeviceHistoryOneCount(context *gin.Context) {
	count, err := dal.GetDeviceHistoryOneCount()
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}
	context.JSON(http.StatusOK, count)
}

func GetDeviceHistoryTwoCount(context *gin.Context) {
	count, err := dal.GetDeviceHistoryTwoCount()
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}
	context.JSON(http.StatusOK, count)
}

func GetFlowAreaACount(context *gin.Context) {
	count, err := dal.GetFlowAreaACount()
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}
	context.JSON(http.StatusOK, count)
}

func GetFlowAreaBCount(context *gin.Context) {
	count, err := dal.GetFlowAreaBCount()
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}
	context.JSON(http.StatusOK, count)
}

func GetPortableDeviceCount(context *gin.Context)  {
	count, err := dal.GetPortableDeviceCount()
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}
	context.JSON(http.StatusOK, count)
}

func GetSleetCount(context *gin.Context) {
	count, err := dal.GetSleetCount()
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}
	context.JSON(http.StatusOK, count)
}

func GetDataErrorLogCount(context *gin.Context) {
	count, err := dal.GetDataErrorLogCount()
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}
	context.JSON(http.StatusOK, count)
}

func GetSystemErrorLogCount(context *gin.Context) {
	count, err := dal.GetSystemErrorLogCount()
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}
	context.JSON(http.StatusOK, count)
}
