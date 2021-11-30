# unity常用资料

- Vector2变量类型：一种存储两个数字的数据类型，存贮在Inspector面板里关于transform组件中positon的x,y值。

- 如果想要游戏物体以每秒多少的速度移动可以乘上Time.deltaTime

- 代码的注释使用“//”，多行注释快捷键ctrl+k+c,解除注释ctrl+k+u

- 根据游戏对象的某个轴向去绘制游戏对象：Edit > Project Settings > Graphics > Camera Settings > Transparency Sort Mode，调整想要决定绘制的轴向，值的正负决定是大或小的先绘制，例如：Y:1，则Y坐标越小的游戏对象越后绘制（渲染），我们可以看到，不会被遮挡。Y：-1，则相反。

- 发生碰撞检测的必要条件：双方必须都有碰撞器，且一方有刚体，最好是运动的一方。因为Unity为了性能的优化，刚体长时间不发生碰撞检测会休眠。

- 2D游戏物体因为碰撞受力会发生Z轴上的角度旋转，可以通过Rigidbody2D>Constraints>FreezeRotation去冻结Z轴上的角度旋转。

- 2D游戏物体之所以碰撞会发生抖动，是因为物理系统控制的位移与开发者编写代码产生的位移起了冲突，需要使用

物理系统里的位移方式来进行位移，也就是借助刚体组件的移动方法来移动。

- 静态方法的调用：类名.方法名（参数），全局可访问，不需要实例。普通方法的调用：对象名.方法名（参数）。

1. 变量赋值顺序：声明变量后直接赋值先于Inpector赋值先于Start方法里的赋值

2. 触发器（Trigger）：触发某一个事件的机关。在BoxCollider组件中把isTrigger属性勾上可以把碰撞器做成触发器。

3. 发生触发检测的必要条件：双方必须都有碰撞器，其中一方得是触发器，且一方有刚体，最好是运动的一方。

4. 在脚本中gameObject指当前脚本挂载的游戏物体对象，transform指当前脚本挂载游戏物体对象身上的transform组件。

5. 为了使某个变量只能够在内部修改，外部只读，可以给它制作一个属性值。

6. 触发检测调用的方法：OnTriggerEnter（进入触发器触发）,OnTriggerStay（在触发器内每帧触发），OnTriggerExit（出来触发器触发）。

7. 碰撞检测调用的方法：OnCollisionEnter，OnCollisionStay，OnCollisionExit。

8. 如果想要获取碰撞到的游戏物体可以使用Collision类型的对象.gameObject的形式获取，进而可以获取该游戏物体身上挂载的某个组件。

9. 动画控制器（Animator Controller）：根据当前游戏对象的状态控制播放对应的游戏动画。也可以叫做动画状态机。

10. 在代码中获取Animator组件之后可以使用set+变量类型的方法去设置状态机里的参数值。

11. Vector类型的变量既可以用来表示坐标，也可以用来表示向量。

12. Mathf.Approximately(a,b)可以用来判断两个浮点数a,b之间是否近似相等。

13. a.Normalize()方法可以用来使向量a单位化。a.magnitude是可以取到当前a的向量模长。

14. 通过物理系统给游戏对象施加力的效果，需要先获取到刚体组件，然后调用AddForce()方法。

15. 监听玩家按下某个按键可以使用Input.GetKeyDown(KeyCode.* )，* 代表某个按键。

16. 实例化（Instantiate）：如果想要动态生成一个游戏物体，需要调用实例化方法来对预制体进行克隆。第一个参数是想要克隆的预制体资源，第二个参数是需要生成到的位置，第三个参数是旋转角度。旋转角度跟检视面板里显示的是不一样的，是一个四元数类型的参数，不是Vector3类型的参数。

17. Quaternion.identity表示预制体默认旋转角度。

18. 层级（Layer）是Unity中场景物体的一种属性。可用于设置物理碰撞关系。

19. 设置是否发生碰撞检测的层级Edit > Project Settings > Physics 2D，另外对应的游戏物体右上角要去设置对应的层级。

20. 想要让某个游戏物体的刚体从当前物理系统中移除，不再发生碰撞检测，可以使用rigidbody2d.simulated=false

21. Cinemachine工具包可以快速创建复杂的相机设置，允许在多个相机之间移动，跟随和剪切。

22. 规定摄像机边界，可以给地形做一个碰撞器边界，在CMvcanm里的cinemachineCOnfiner中的Boundingshape2D设置一个带有PolygonConllider2D或是CompositeCollider2D的碰撞器的空游戏对象。

23. 在Hierachy窗口中右键点击Effect>ParticleSystem可创建粒子系统。

24. 如果想要在多个图片资源中随机产生则需要将StartFrame选项的Constant改为Random Between Two Constants。常量代表的是使用的资源索引。

25. 如果不想要粒子在播放中更换图片资源，则需要将FrameOverTime的动画曲线设置为水平点，即删除线段末尾的关键帧点。

26. 在粒子系统基础属性里，将Simulation Space的值从Local改为world，粒子就不会跟随游戏物体进行移动了。

27. 想要在一段时间爆发产生大部分粒子可以使用Emission属性。

28. 选中Image，点击组件中的Set Native Size按钮可以使图片保持原本大小。

29. 不规则图形的填充可以使用mask组件，父对象UI需要挂载mask组件，子对象则为具体填充UI。

30. 想要全局访问某一个变量的方法或者成员变量可以使用单例模式。

31. 音效的播放可以使用AudioSouce组件的PlayOneShot方法。

32. 使用随机数可以使用Random.Range（a,b）方法，如果a,b为整数int，则随机数包含a,不包含b，如果是浮点数，则左右都包含。

33. 音频源（AudioSouce）:音频源是一个组件，允许在组件所在的GameObject位置播放音频剪辑。

34. 如果想要播放持续音效，可以直接调用audioSouce.Play（），停止则可以使用audioSouce.Stop（），是否正在播放状态的判断可以使用audioSouce.isplaying

35. bool的默认值是flase，int和float是0。

36. Unity打包后的玩家可执行应用程序称为player，在 Edit > Project Settings > Player可设置player的一些配置参数。

37. 游戏中如果没有设置退出，可以使用快捷键退出，在Windows/Linux上按ALT+F4或在Mac OSX上按Command+Q退出。

38. 每次打包要换一个文件夹以及产品名称新设定的一些属性才可以在游戏包中起作用。

    

