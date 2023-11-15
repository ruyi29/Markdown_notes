## __attribute__((packed))
```
	typedef struct {
		double x;
		double y;
	} __attribute__((packed)) position_t;
```
- `__attribute__ ((packed))` 的作用是告诉编译器: 取消结构在编译过程中的优化对齐,按照实际占用字节数进行对齐，是GCC特有的语法.
- 减小占用的空间
  - 在TC下：struct my{ char ch; int a;}  （紧凑模式）
    - sizeof(int)=2
    - sizeof(my)=3
  - 在GCC下：struct my{ char ch; int a;}  （非紧凑模式）
    - sizeof(int)=4
    - sizeof(my)=8
  - 在GCC下：struct my{ char ch; int a;}__attrubte__ ((packed)) 
    - sizeof(int)=4
    - sizeof(my)=5
- __attribute__可以设置: 函数属性（Function Attribute）、变量属性（Variable Attribute）和类型属性（Type Attribute）

## explicit
```
class Sensor:
  protected:
      // 构造函数
      explicit Sensor();
      // 重写基类的 Update 方法
      void Update() override;
```
- 声明只能以显式调用的方式进行初始化的构造函数，保护构造函数
- 当构造函数被声明为explicit时，它将不再允许隐式转换或复制初始化，只能通过直接调用来创建对象。

## override
```
class Sensor:
  protected:
      // 构造函数
      explicit Sensor();
      // 重写基类的 Update 方法
      void Update() override;
```
- 表示派生类中的Update方法将会覆盖（重写）基类中的同名虚函数。
- 通过使用override关键字，可以帮助开发者在编译时捕获一些常见的错误，比如拼写错误或者意外地未能覆盖基类中的虚函数。