#!/usr/bin/node
/**
 * function returns reversed version of a list
 * @param list
 * @returns {*[]}
 */
exports.esrever = function (list){
    let rList = []
    let item = list.length -1;
    for (item; item >= 0; item--){
        rList.push(list[item]);
    }
    return rList;
}