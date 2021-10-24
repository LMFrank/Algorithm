package main

import (
	"fmt"
	"sync"
)

type Array struct {
	array []int // 固定大小的数组，用满容量和满大小的切片来代替
	len   int   // 真正长度
	cap   int   // 容量
	lock  sync.Mutex
}

func Make(len, cap int) *Array {
	s := new(Array)
	if len > cap {
		panic("len larger than cap")
	}

	// 把切片当数组用
	array := make([]int, cap, cap)

	s.array = array
	s.cap = cap
	s.len = 0
	return s
}

// Append 增加一个元素
func (a *Array) Append(element int) {
	a.lock.Lock()
	defer a.lock.Unlock()

	if a.len == a.cap {
		newCap := 2 * a.Len()

		if a.cap == 0 {
			newCap = 1
		}

		newArray := make([]int, newCap, newCap)

		for k, v := range a.array {
			newArray[k] = v
		}

		a.array = newArray
		a.cap = newCap
	}

	a.array[a.len] = element
	a.len = a.len + 1
}

// AppendMany 增加多个元素
func (a *Array) AppendMany(element ...int) {
	for _, v := range element {
		a.Append(v)
	}
}

// Get 获取某个下标的元素
func (a *Array) Get(index int) int {
	if a.len == 0 || index >= a.len {
		panic("index over len")
	}
	return a.array[index]
}

// Len 返回真实长度
func (a *Array) Len() int {
	return a.len
}

// Cap 返回容量
func (a *Array) Cap() int {
	return a.cap
}

// Print 辅助打印
func Print(array *Array) (result string) {
	result = "["
	for i := 0; i < array.Len(); i++ {
		if i == 0 {
			result = fmt.Sprintf("%s%d", result, array.Get(i))
			continue
		}

		result = fmt.Sprintf("%s %d", result, array.Get(i))
	}

	result = result + "]"
	return
}

func main() {
	a := Make(0, 3)
	fmt.Println("cap", a.Cap(), "len", a.Len(), "array:", Print(a))

	// 增加一个元素
	a.Append(10)
	fmt.Println("cap", a.Cap(), "len", a.Len(), "array:", Print(a))
	// 增加一个元素
	a.Append(9)
	fmt.Println("cap", a.Cap(), "len", a.Len(), "array:", Print(a))
	// 增加多个元素
	a.AppendMany(8, 7)
	fmt.Println("cap", a.Cap(), "len", a.Len(), "array:", Print(a))
}
