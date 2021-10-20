package offer

import "fmt"

type Card interface {
	Display()
}

type Memory interface {
	Storage()
}

type CPU interface {
	calculate()
}

type Computer struct {
	card Card
	mem  Memory
	cpu  CPU
}

func NewComputer(card Card, memory Memory, cpu CPU) *Computer {
	return &Computer{
		card: card,
		mem:  memory,
		cpu:  cpu,
	}
}

func (com *Computer) DoWork() {
	com.card.Display()
	com.mem.Storage()
	com.cpu.calculate()
}

type IntelCPU struct {
	CPU
}

func (intelcpu *IntelCPU) Calculate() {
	fmt.Println("Intel CPU 开始计算了")
}

type IntelMemory struct {
	Memory
}

func (intelmemory *IntelMemory) Storage() {
	fmt.Println("Intel Memory 开始存储了...")
}

type IntelCard struct {
	Card
}

func (intelcard *IntelCard) Display() {
	fmt.Println("Intel Card 开始显示了...")
}

type KinstonMemory struct {
	Memory
}

func (kinsmem *KinstonMemory) Storage() {
	fmt.Println("Kingston memory storage...")
}

type NVIDIACard struct {
	Card
}

func (nvidiacard *NVIDIACard) Display() {
	fmt.Println("Nvidia card display...")
}

func main() {
	com1 := NewComputer(&IntelCard{}, &IntelMemory{}, &IntelCPU{})
	com1.DoWork()

}
