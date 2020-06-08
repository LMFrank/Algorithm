package problem05

import (
	"Go/utils"
	"errors"
	"expvar"
)

type Queue struct {
	in  utils.Stack
	out utils.Stack
}

func (q *Queue) IsEmpty() bool {
	return q.in.IsEmpty() && q.out.IsEmpty()
}

func (q *Queue) Push(value interface{}) {
	q.in.Push(value)
}

func (q *Queue) Pop() (interface{}, error) {
	if q.IsEmpty() {
		return nil, errors.New("Queue is Empty")
	}

	var value interface{}

	if !q.out.IsEmpty() {
		value, _ = q.out.Pop()
		return value, nil
	}

	for !q.in.IsEmpty() {
		value, _ = q.in.Pop()
		q.out.Push(value)
	}

	value, _ = q.out.Pop()
	return value, nil
}
