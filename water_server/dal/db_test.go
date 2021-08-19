package dal

import (
	"testing"
)

func TestDB(t *testing.T)  {
	var systemErrorLogs []*SystemErrorLog
	_ = DB.Model(&SystemErrorLog{}).Find(&systemErrorLogs)
	for _, v := range systemErrorLogs {
		t.Logf("%v\n", v)
	}
}
