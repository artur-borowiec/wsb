fun main() {    
    assert(toASCII('C') == 67)
    assert(toASCII("C") == listOf(67))
   	assert("!AB*".toBinary() == "10000110000011000010101010")
}

fun toASCII(input: String): List<Int> =
    input.toCharArray().map { toASCII(it) }

fun toASCII(input: Char): Int {
    val output = input.code
    
    return output
}

//TODO: replace toBinaryString with manual operation 
fun String.toBinary() =
    toASCII(this).map { Integer.toBinaryString(it) }.joinToString("")
	
