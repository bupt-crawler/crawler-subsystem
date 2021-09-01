package validation

import (
	"testing"
)

func TestPinger(t *testing.T)  {
	pinger := NewPinger([]string{"gprs.sj2000.org", "159.226.153.6"})
	pinger.Ping()
}
