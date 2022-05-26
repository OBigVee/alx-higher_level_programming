#!/usr/bin/node
/**
 * Number conversion
 * @param base
 * @returns {function(*): string}
 */
exports.converter = function (base){
    function convert (num){
        return num.toString(base);
    }
    return convert;
}