package validation

import (
	"errors"
	"reflect"
	"strconv"
)

var (
	InvalidParamTypeError = errors.New("invalid param type")
)

type MapValidation struct {
	FieldMap map[string]interface{}
	Model    interface{}
}

func NewMapValidation(fieldMap map[string]interface{}, model interface{}) *MapValidation {
	return &MapValidation{
		FieldMap: fieldMap,
		Model:    model,
	}
}

func (h *MapValidation) Validate() error {
	var err error
	fields := reflect.ValueOf(h.Model).Elem()
	for i := 0; i < fields.NumField(); i++ {
		jsonName := fields.Type().Field(i).Tag.Get("json")
		var mapValue interface{}
		var ok bool
		if mapValue, ok = h.FieldMap[jsonName]; !ok {
			continue
		}
		switch fields.Field(i).Kind() {
		case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
			if _, err = strconv.Atoi(mapValue.(string)); err != nil {
				return InvalidParamTypeError
			}
		case reflect.Uint, reflect.Uint8, reflect.Uint16, reflect.Uint32, reflect.Uint64:
			if _, err = strconv.ParseUint(mapValue.(string), 10, 64); err != nil {
				return InvalidParamTypeError
			}
		case reflect.Float32, reflect.Float64:
			if _, err = strconv.ParseFloat(mapValue.(string), 64); err != nil {
				return InvalidParamTypeError
			}
		case reflect.Bool:
			if _, err = strconv.ParseBool(mapValue.(string)); err != nil {
				return InvalidParamTypeError
			}
		case reflect.Slice:
			value := mapValue.(string)
			if len(value) < 2 {
				return InvalidParamTypeError
			}
			if value[0] != '[' && value[len(value)-1] != ']' {
				return InvalidParamTypeError
			}
		}
	}
	return nil
}
