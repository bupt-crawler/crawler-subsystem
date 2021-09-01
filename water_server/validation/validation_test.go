package validation

import (
	jsoniter "github.com/json-iterator/go"
	"testing"
)

func TestMapValidation_Validate(t *testing.T) {
	type Test struct {
		I      int     `json:"i"`
		U      uint    `json:"u"`
		F      float64 `json:"f"`
		B      bool    `json:"b"`
		S      string  `json:"s"`
		Slice  []int   `json:"slice"`
	}

	data := make(map[string]interface{})
	err := jsoniter.UnmarshalFromString(`{"i": "1", "u": "2", "f": "3.3", "b": "true", "s": "string", "slice": "[1, 2, 3]"}`, &data)
	if err != nil {
		t.Errorf("%v\n", err)
		return
	}
	t.Logf("%v\n", data)
	err = NewMapValidation(data, &Test{}).Validate()
	if err != nil {
		t.Errorf("%v\n", err)
		return
	}
}
