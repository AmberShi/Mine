h = "substring"
    , i = "split"
    , j = "replace"
    , k = "substr";
 
 
function getHex(a) {
    return {
        str: a[h](4),
        hex: a[h](0, 4)[i]("").reverse().join("")
    }
}
 
 
function getDec(a) {
    var b = parseInt(a, 16).toString();
    return {
        pre: b[h](0, 2)[i](""),
        tail: b[h](2)[i]("")
    }
}
 
 
function substr(a,b) {
    var c = a[h](0, b[0])
        , d = a[k](b[0], b[1]);
    return c + a[h](b[0])[j](d, "")
}
 
 
function getPos(a,b) {
    return b[0] = a.length - b[0] - b[1],
        b
}
 
 
function atob(a) {
    var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    if (a = a.replace(/=+$/, ""),
    a.length % 4 == 1)
        throw f;
    for (var b, c, d = 0, g = 0, h = ""; c = a.charAt(g++); ~c && (b = d % 4 ? 64 * b + c : c,
    d++ % 4) ? h += String.fromCharCode(255 & b >> (-2 * d & 6)) : 0)
        c = e.indexOf(c);
    return h
}
 
function main(a) {
    var b = getHex(a)
        , c = getDec(b.hex)
        , d = substr(b.str, c.pre);
    zz = substr(d, getPos(d, c.tail));
    return atob(zz)
}
 
 
//a = '55e0aHRVhJYAS0cDovL212dmlkZW8xMC5tZWl0dWRhdGEuY29tLzVkMzNmMGRmM2RkYzRwMm5sd3N0cWg3OTA2X0gyNjRfMV85YzNiM2QwOTNhMWRhNS5tcDQ/az1kODlkOTVmZmRlNWZjNzQ0YzUwOTY0NDZiZjNhNTE0OCZ0PTVkNDEIQbtCanOZiOWY4'
//console.log(main(a))