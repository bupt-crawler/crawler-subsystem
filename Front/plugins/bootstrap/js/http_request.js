'use strict'

var HOST = 'http://120.53.104.59:8080/'

function httpRequest(url, method, success, error, async) {
    $.ajax({
        "url": url,
        "type": method,
        "dataType": "json",
        "success": success,
        "error": error,
        "async": async
    })
}

function getRequest(url, success, error, async = false) {
    return httpRequest(url, "GET", success, error, async)
}

function postRequest(url, success, error, async = false) {
    return httpRequest(url, "POST", success, error, async)
}

function getRequestResult(url, error) {
    let result
    getRequest(url, (data) => {
        result = data
    }, error)
    return result
}

function postRequestResult(url, error) {
    let result
    postRequest(url, (data) => {
        result = data
    }, error)
    return result
}

function getDeviceHistoryOne(offset, count, error) {
    let url = HOST + 'water/device_history_one?'
    if (offset != null) url += 'offset=' + offset + '&'
    if (count != null) url += 'count=' + count
    return getRequestResult(url, error)
}

function getDeviceHistoryOneCount(error) {
    let url = HOST + 'count/device_history_one'
    return getRequestResult(url, error)
}

function getDeviceHistoryTwo(offset, count, error) {
    let url = HOST + 'water/device_history_two?'
    if (offset != null) url += 'offset=' + offset + '&'
    if (count != null) url += 'count=' + count
    return getRequestResult(url, error)
}

function getDeviceHistoryTwoCount(error) {
    let url = HOST + 'count/device_history_two'
    return getRequestResult(url, error)
}

function getFlowAreaAResult(offset, count, error) {
    let url = HOST + 'water/flow_area_a?'
    if (offset != null) url += 'offset=' + offset + '&'
    if (count != null) url += 'count=' + count
    return getRequestResult(url, error)
}

function getFlowAreaACount(error) {
    let url = HOST + 'count/flow_area_a'
    return getRequestResult(url, error)
}

function getFlowAreaBResult(offset, count, error) {
    let url = HOST + 'water/flow_area_b?'
    if (offset != null) url += 'offset=' + offset + '&'
    if (count != null) url += 'count=' + count
    return getRequestResult(url, error)
}

function getFlowAreaBCount(error) {
    let url = HOST + 'count/flow_area_b'
    return getRequestResult(url, error)
}

function getPortableDeviceResult(offset, count, error) {
    let url = HOST + 'water/portable_device?'
    if (offset != null) url += 'offset=' + offset + '&'
    if (count != null) url += 'count=' + count
    return getRequestResult(url, error)
}

function getPortableDeviceCount(error) {
    let url = HOST + 'count/portable_device'
    return getRequestResult(url, error)
}

function getSleetResult(offset, count, error) {
    let url = HOST + 'water/sleet?'
    if (offset != null) url += 'offset=' + offset + '&'
    if (count != null) url += 'count=' + count
    return getRequestResult(url, error)
}

function getSleetCount(error) {
    let url = HOST + 'count/sleet'
    return getRequestResult(url, error)
}

function getSystemErrorLogResult(offset, count, error) {
    let url = HOST + 'water/system_error_log?'
    if (offset != null) url += 'offset=' + offset + '&'
    if (count != null) url += 'count=' + count
    return getRequestResult(url, error)
}

function getSystemErrorLogCount(error) {
    let url = HOST + 'count/system_error_log'
    return getRequestResult(url, error)
}

function getDataErrorLogResult(offset, count, error) {
    let url = HOST + 'water/data_error_log?'
    if (offset != null) url += 'offset=' + offset + '&'
    if (count != null) url += 'count=' + count
    return getRequestResult(url, error)
}

function getDataErrorLogCount(error) {
    let url = HOST + 'count/data_error_log'
    return getRequestResult(url, error)
}
