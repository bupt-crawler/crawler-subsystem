package main

import (
	"github.com/gin-gonic/gin"
	"log"
	"net/http"
	"water_server/consts"
	_ "water_server/dal"
	"water_server/handler"
	"water_server/kafka"
	_ "water_server/kafka"
	"water_server/validation"
)

func main() {
	router := gin.Default()

	// only for test
	//router.Use(cors)

	urls := []string{}
	for k, _ := range consts.URLs {
		urls = append(urls, k)
	}
	validation.NewPinger(urls).Schedule(consts.PingInterval)

	waterRouter := router.Group("/water")
	{
		waterRouter.GET("/device_history_one", handler.GetDeviceHistoryOne)
		waterRouter.GET("/device_history_two", handler.GetDeviceHistoryTwo)
		waterRouter.GET("/flow_area_a", handler.GetFlowAreaA)
		waterRouter.GET("/flow_area_b", handler.GetFlowAreaB)
		waterRouter.GET("/portable_device", handler.GetPortableDevice)
		waterRouter.GET("/sleet", handler.GetSleet)
		waterRouter.GET("/system_error_log", handler.GetSystemErrorLog)
		waterRouter.GET("/data_error_log", handler.GetDataErrorLog)
	}

	countRouter := router.Group("/count")
	{
		countRouter.GET("/device_history_one", handler.GetDeviceHistoryOneCount)
		countRouter.GET("/device_history_two", handler.GetDeviceHistoryTwoCount)
		countRouter.GET("/flow_area_a", handler.GetFlowAreaACount)
		countRouter.GET("/flow_area_b", handler.GetFlowAreaBCount)
		countRouter.GET("/portable_device", handler.GetPortableDeviceCount)
		countRouter.GET("/sleet", handler.GetSleetCount)
		countRouter.GET("/system_error_log", handler.GetSystemErrorLogCount)
		countRouter.GET("/data_error_log", handler.GetDataErrorLogCount)
	}

	router.GET("/", func(context *gin.Context) {
		context.Redirect(http.StatusPermanentRedirect, "/crawlerFront/index.html")
	})
	router.Static("/crawlerFront", "./resource/Front/crawlerFront")
	router.Static("/css", "./resource/Front/css")
	router.Static("/img", "./resource/Front/img")
	router.Static("/plugins", "./resource/Front/plugins")

	router.Run(":8080")
	kafka.Consumer.Close()
}

func cors(c *gin.Context) {
	method := c.Request.Method
	origin := c.Request.Header.Get("Origin")
	if origin != "" {
		c.Writer.Header().Set("Access-Control-Allow-Origin", origin)
		c.Header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE, UPDATE")
		c.Header("Access-Control-Allow-Headers", "Authorization, Content-Length, X-CSRF-Token, Token, session")
		c.Header("Access-Control-Expose-Headers", "Content-Length, Access-Control-Allow-Origin, Access-Control-Allow-Headers")
		c.Header("Access-Control-Max-Age", "172800")
		c.Header("Access-Control-Allow-Credentials", "true")
	}
	if method == "OPTIONS" {
		c.JSON(http.StatusOK, "ok!")
	}
	defer func() {
		if err := recover(); err != nil {
			log.Printf("Panic info is: %v\n", err)
		}
	}()
	c.Next()
}
