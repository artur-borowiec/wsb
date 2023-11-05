fun main() {
    compress("AAAAAAB")
    
    assert(compress("AAAAAABBBAAABBA") == "6A3B3A2B1A")
    assert(compress("C") == "1C")
    assert(compress("CAB") == "1C1A1B")
    assert(compress("CC") == "2C")
}

fun compress(input: String): String {
    var char = ""
    var count = 0
    
    var output = ""
    
    input.forEach {
        if (char == "") {
            char = it.toString()
            count += 1
        }
        else if (char == it.toString()) {
            count += 1
        }
        else if (char != it.toString()) {
            output += "$count$char"
            char = it.toString()
            count = 1
        }
    }
    output += "$count$char"
    
    println(output)
    
    return output
}
