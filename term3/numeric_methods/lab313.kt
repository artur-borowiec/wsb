fun main() {    
    assert('W'.shift(-2) == 'U')
    assert('A'.shift(-2) == 'Y')
}

fun Char.shift(value: Int): Char {
    var shifted = this
    if (this.isLowerCase()) {
    	val shiftedAscii = (toASCII(this) + value).toChar()
        if (shiftedAscii < 61) shifte 
    }
    else if (this.isUpperCase()) {
        val shiftedAscii = (toASCII(this) + value).toChar()
    }
    
    return shifted
}

fun toASCII(input: String): List<Int> =
    input.toCharArray().map { toASCII(it) }

fun toASCII(input: Char) = input.code
