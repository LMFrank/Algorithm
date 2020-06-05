package problem02

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

type para struct {
	str string
}

type ans struct {
	res string
}

type question struct {
	p para
	a ans
}

func Test_OK(t *testing.T) {
	ast := assert.New(t)

	qs := []question{
		question{
			p: para{
				str: "We are happy.",
			},
			a: ans{
				res: "We%20are%20happy.",
			},
		},
	}

	for _, q := range qs {
		a, p := q.a, q.p
		res := replaceSpace(p.str)
		ast.Equal(a.res, res, "输入:%v", p)
	}
}
