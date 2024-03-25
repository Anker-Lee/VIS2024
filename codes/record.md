这是一个大的任务，我们可以将其分解为以下几个步骤：

1. 存储场景信息：创建一个数据结构（例如数组或对象），用于存储每个场景的布局信息。这可能包括元素的位置、大小、颜色等属性。

2. 创建动画函数：为每个可能的动画创建一个函数。这些函数应该接受一个场景作为参数，并返回一个新的场景，表示动画结束后的状态。

3. 尝试动画：当用户选择一个动画时，使用该动画的函数和当前场景作为参数，生成一个新的场景。然后，将新的场景显示给用户。

4. 记录动画：当用户确定一个动画后，将该动画的函数和参数添加到一个列表中。这个列表将用于在最后播放所有的动画。

5. 播放动画：当用户点击播放时，从第一个场景和动画列表开始，依次执行每个动画。在每个动画之后，都应该更新当前的场景。

以下是这个想法的伪代码：

```javascript
let scenes = []; // 存储每个场景的信息
let animations = []; // 存储每个动画的函数和参数

function tryAnimation(animation, scene) {
    // 使用动画函数和当前场景生成新的场景
    let newScene = animation(scene);
    // 显示新的场景给用户
    displayScene(newScene);
}

function confirmAnimation(animation, scene) {
    // 将动画的函数和参数添加到列表中
    animations.push({func: animation, args: scene});
    // 更新当前的场景
    scenes.push(scene);
}

async function playAnimations() {
    // 从第一个场景开始
    let currentScene = scenes[0];
    // 依次执行每个动画
    for (let i = 0; i < animations.length; i++) {
        let animation = animations[i];
        currentScene = await animation.func(currentScene, animation.args);
        // 在每个动画之后，都更新当前的场景
        displayScene(currentScene);
    }
}
```

这只是一个基本的框架，你可能需要根据你的具体需求进行修改。例如，你可能需要添加更多的函数来处理用户的输入，或者修改 `displayScene` 函数来显示场景的具体内容。



为了能够回到某个中间场景并调整动画，你需要在数据结构中存储每个场景的状态以及与之关联的动画。这样，当需要回到某个特定场景时，你可以从数据结构中获取该场景的状态，并将其加载到你的应用中。

以下是一个可能的实现方式：

1. 在你的数据结构中，为每个场景存储一个状态对象。这个对象应该包含足够的信息来完全重建该场景。

2. 当用户选择要回到的场景时，从数据结构中获取该场景的状态对象，并使用这个对象来重建场景。

3. 允许用户修改场景并尝试新的动画。当用户满意并确认动画后，更新数据结构中的场景状态和关联的动画。

以下是这个想法的伪代码：

```javascript
let scenes = []; // 存储每个场景的状态
let animations = []; // 存储每个动画的函数和参数

function goToScene(index) {
    // 获取场景的状态
    let sceneState = scenes[index];
    // 重建场景
    let scene = rebuildScene(sceneState);
    // 显示场景
    displayScene(scene);
}

function updateScene(index, scene, animation) {
    // 更新场景的状态
    scenes[index] = getSceneState(scene);
    // 更新关联的动画
    animations[index] = {func: animation.func, args: animation.args};
}
```

在这个例子中，`rebuildScene` 函数根据给定的状态对象重建一个场景，`getSceneState` 函数获取一个场景的状态对象。这两个函数的具体实现取决于你的应用的具体需求。




你可以通过将 `story_board` div 的 `innerHTML` 属性保存到一个变量中来存储特定时刻的场景。`innerHTML` 属性包含了元素的所有 HTML，包括子元素。

然后，你可以通过将 `story_board` div 的 `innerHTML` 属性设置为你保存的值来还原场景。

以下是如何在 JavaScript 中实现这个功能的示例：

```javascript
// 存储场景
let savedScene = document.getElementById('story_board').innerHTML;

// 还原场景
document.getElementById('story_board').innerHTML = savedScene;
```

请注意，这种方法只保存和还原了 HTML 结构，不包括 JavaScript 事件处理程序和 CSS 动画状态。如果你的场景包含这些内容，你可能需要使用更复杂的方法来保存和还原场景。

例如，你可能需要使用 `cloneNode(true)` 方法来复制 `story_board` div 和它的所有子节点，包括事件处理程序。然后，你可以将复制的节点保存在一个变量中，以便以后使用。然后，你可以通过删除 `story_board` div 的所有子节点，然后将复制的节点添加回去来还原场景。

另外，如果你的场景包含 CSS 动画，你可能需要保存动画的当前状态，然后在还原场景时恢复这些状态。这可能需要使用 Web Animations API 或其他 JavaScript 动画库来实现。



在你的 `loadScene` 方法中，你是从 `this.scenes` 数组中获取一个已经保存的场景（也就是一个已经克隆的 `storyBoard` 元素），然后用这个克隆的元素替换当前的 `storyBoard` 元素。这个克隆的元素是在你调用 `saveScene` 方法时创建的，它包含了那时 `storyBoard` 元素的状态（包括所有子元素的位置）。

然而，你的 `loadScene` 方法并没有创建一个新的克隆，而是直接使用了 `this.scenes` 数组中的元素。这意味着，当你更改布局并重新绑定事件后，你实际上是在修改 `this.scenes` 数组中的元素。因此，当你再次调用 `loadScene` 方法时，你看到的是你最后一次修改的结果，而不是你最初保存的布局。

为了解决这个问题，你需要在 `loadScene` 方法中创建一个新的克隆，而不是直接使用 `this.scenes` 数组中的元素。这样，你就可以保留你最初保存的布局，而不会被后续的修改影响。

以下是修改后的 `loadScene` 方法：

```vue
loadScene(index = 0) {
    // 创建一个新的克隆
    const clonedStoryBoard = this.scenes[index].cloneNode(true);

    const storyBoard = document.getElementById("story_board");
    storyBoard.replaceWith(clonedStoryBoard);

    // 重新绑定事件
    this.animateShape();
    // 遍历 storyBoard子元素，并根据class筛选
    const items = clonedStoryBoard.querySelectorAll(".item_in_story");
    items.forEach(item => {
        item.addEventListener('click', event => this.handle_emoji_click(event));
    });

    const characters = clonedStoryBoard.querySelectorAll(".character_in_story");
    characters.forEach(character => {
        console.log(character);
        character.addEventListener('click', event => this.handle_emoji_click(event));
    });
},
```

这样，每次调用 `loadScene` 方法时，你都会创建一个新的克隆，这个克隆包含了你最初保存的布局。因此，无论你如何修改布局，只要你没有调用 `saveScene` 方法，你都可以通过调用 `loadScene` 方法恢复到你最初保存的布局。



你的 `resolve()` 函数确实在 `move_head` 函数的最后被调用了，但是这并不意味着它在动画完成后被调用。`gsap.fromTo` 是一个异步操作，它不会阻塞代码的执行。这意味着在 `gsap.fromTo` 开始动画之后，代码会立即继续执行，`resolve()` 函数会被立即调用，而不是在动画完成后调用。

你需要将 `resolve()` 函数放在 `gsap` 动画的 `onComplete` 回调中，这样它就会在动画完成后被调用。你可以这样修改你的代码：

```vue
move_head(objectId, range = 60, repeatTime = 4, duration = 0.4, resolve = null) { // 摇头
    let object = document.getElementById(objectId);

    const defaultResolve = () => { };
    if (resolve === null) {
        resolve = defaultResolve;
    }

    if (object === null) {
        console.log("object is null");
        return;
    }
    if (object.classList.contains("emoji_head") === false) {
        return;
    }
    gsap.fromTo(object, { rotateY: -range }, {
        rotateY: range, 
        ease: "power1.inOut", 
        repeat: repeatTime, 
        yoyo: true, 
        duration: duration, 
        onComplete: function () {
            gsap.to(object, { rotateY: 0, ease: "power1.inOut", duration: duration / 2, onComplete: resolve });
        }
    });

    if (resolve === defaultResolve) {
        this.userAnimationsCache.push({ func: this.move_head, args: [objectId, range, repeatTime, duration] });
        console.log("this.userAnimationsCache: ", this.userAnimationsCache);
    }
},
```

这样，`resolve()` 函数会在动画完成后被调用，这将导致 `new Promise` 在动画完成后解决，从而使动画按顺序执行。