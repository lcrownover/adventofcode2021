package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func getFileText() string {
    content, err := ioutil.ReadFile("inputs.txt")
    if err != nil {
        panic(err)
    }
    return string(content)
}

func to_i(s string) int {
    i, _ := strconv.Atoi(s)
    return i
}

func deleteEmpty(s []string) []string {
    var r []string
    for _,str := range s {
        if str != "" {
            r = append(r, str)
        }
    }
    return r
}

func first() {
    inputs := getFileText()
    lines := strings.Split(inputs, "\n")
    entries := deleteEmpty(lines)

    count := 0
    for i := range entries {
        switch i {
        case 0:
            fmt.Println("begin!")
        default:
            curr := to_i(entries[i])
            last := to_i(entries[i-1])
            if curr > last {
                fmt.Println(curr, "< greater")
                count += 1
            } else {
                fmt.Println(curr)
            }
        }
    }
    fmt.Println(count)
}

// type M map[string]interface{}
//
// func second() {
//     inputs := getFileText()
//     lines := strings.Split(inputs, "\n")
//     entries := deleteEmpty(lines)
//
//     var ol []int
//     var ml []M
//     for i,el := range entries {
//         fmt.Println("begin!")
//         switch i {
//         case 0:
//             m1 := M{"count": 1, "total": to_i(el)}
//         case 1:
//             m1 := M{"count": 1, "total": to_i(el)}
//             m2 := ml[len(ml)-1]
//             m2["count"] = to_i()
//         default:
//             m1 := M{"count": 1, "total": to_i(el)}
//             m2 := ml[len(ml)-1]
//             m3 := ml[len(ml)-2]
//
//
//
//
//
//
//             // curr := to_i(entries[i])
//             // last := to_i(entries[i-1])
//             // if curr > last {
//             //     fmt.Println(curr, "< greater")
//             //     count += 1
//             // } else {
//             //     fmt.Println(curr)
//             // }
//         }
//     }
//     fmt.Println(count)
// }

func main() {
    first()
}
