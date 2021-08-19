package validation

import (
	"github.com/go-ping/ping"
	"strconv"
	"time"
	"water_server/consts"
	"water_server/dal"
)

type Pinger struct {
	URLs []string
}

func NewPinger(urls []string) *Pinger {
	return &Pinger{URLs: urls}
}

func (p *Pinger) Ping() {
	for _, url := range p.URLs {
		pinger, err := ping.NewPinger(url)
		if err != nil {
			continue
		}
		pinger.Count = 3
		pinger.Timeout = 3 * time.Second
		err = pinger.Run()
		if err != nil {
			continue
		}
		if pinger.Statistics().PacketLoss > 1e-6 {
			data := map[string]interface{}{
				"url":      url,
				"name":     consts.URLs[url],
				"time":     time.Now(),
				"errorLog": "网站连接失败，丢包率: " + strconv.FormatFloat(pinger.Statistics().PacketLoss*100.0, 'f', 2, 32) + "%",
			}
			_ = dal.Insert(data, &dal.SystemErrorLog{})
		}
	}
}

func (p *Pinger) Schedule(duration time.Duration) {
	ticker := time.NewTicker(duration)
	go func(ticker *time.Ticker) {
		for range ticker.C {
			p.Ping()
		}
	}(ticker)
}
