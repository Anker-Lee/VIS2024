<template>
    <div id="app">
        <div id="title">{{ title }}</div>

        <div class="grid-content scenes" style="height: 1048px; overflow: auto;">
            <div v-for="(scene, index) in story_info" :key="index" class="scene_container">
                <div class="frame">Frame {{ index + 1 }}
                    <!-- <button @click="toggle(index)">Toggle</button> -->
                    <el-switch v-model="toggle_rec[index]" active-color="#13ce66" inactive-color="#ff4949">
                    </el-switch>
                </div>
                <div v-html="scene.text" class="scene_text" @click="handleClick" @mouseover="handleMouseover"
                    @mouseout="handleMouseleave" v-show="!toggle_rec[index]"></div>
                <div v-show="toggle_rec[index]">
                    <div v-for="(e, index) in scene.svo" :key="index" class="grid-content svo_container">
                        <el-row :gutter="10" style="display:flex; align-items: center; padding: 10px;">
                            <el-col :span="5">
                                <div class="svo">{{ e.subject }}</div>
                            </el-col>
                            <el-col :span="5">
                                <div class="svo" style="font-weight: bold;">{{ e.verb }}</div>
                            </el-col>
                            <el-col :span="14">
                                <div class="svo">{{ e.object }}</div>
                            </el-col>
                        </el-row>
                    </div>
                </div>
            </div>
        </div>

        <div class="legend_container" style="position: relative; height: 150px;">
            <div id="legend-title">Legend</div>
            <span class="legend_example" style="color:red; left: 20px; top: 50px;">The Little</span>
            <span class="legend_description" style="left: 180px; top: 50px;">Character</span>
            <span class="legend_example right" style="color:green; left: 420px; top: 50px;">The Little</span>
            <span class="legend_description right" style="left:580px; top: 50px;">Items</span>

            <span class="legend_example" style="color:purple; left: 20px; top: 100px;">Cookie</span>
            <span class="legend_description" style="left: 180px; top: 100px;">Thought & Dialogue</span>
            <span class="legend_example right" style="color:blue; left: 420px; top: 100px;">Eat</span>
            <span class="legend_description right" style="left:580px; top: 100px;">Action</span>
        </div>

        <div class="dropdown" @mouseover="showOptions = true" @mouseleave="showOptions = false">
            <div class="arrow">▼</div>
            <div class="options" v-show="showOptions">
                <div class="option" @click="selectOption('Option 1')">Option 1</div>
                <div class="option" @click="selectOption('Option 2')">Option 2</div>
                <div class="option" @click="selectOption('Option 3')">Option 3</div>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    data() {
        return {
            title: "Little Red Riding Hood",
            hoveredIndex: null,
            story_info: [],
            toggle_rec: {},
            actions: [
                {
                    subject: "Little Red Riding Hood",
                    verb: "walked",
                    object: "to the forest"
                },
                {
                    subject: "Little Red Riding Hood",
                    verb: "met",
                    object: "the wolf"
                },
            ],




            showOptions: true,
            selectedOption: null,
        };
    },
    mounted() {
        this.$bus.$on("pass_story_info", (story_info) => {
            // story_info.forEach((_, index) => {
            //     this.$set(this.toggle_rec, index, true);
            // });
            this.story_info = story_info;
            // this.story_info.forEach((_, index) => {
            //     this.$set(this.toggle_rec, index, true);
            // });
        })
    },
    computed: {
    },
    methods: {
        handleClick(event) {
            // 检查是否点击的是带有`marked`类的span
            if (event.target.classList.contains('marked')) {
                // 可以在这里处理你的点击事件
                console.log('Clicked on marked element:', event.target);
            }
        },
        handleMouseover(event) {
            if (event.target.classList.contains('marked')) {
                console.log('mouse over:', event.target);
                event.target.style.backgroundColor = "yellow";
            }
        },
        handleMouseleave(event) {
            if (event.target.classList.contains('marked')) {
                console.log('mouse leave:', event.target);
                event.target.style.backgroundColor = "";
            }
        },
        toggle(index) {
            this.$set(this.toggle_rec, index, !this.toggle_rec[index]);
        },




        selectOption(option) {
            this.selectedOption = option;
            this.showOptions = false;
        },
    },
};
</script>

<style>
.dropdown {
    position: relative;
    display: inline-block;
}

.arrow {
    cursor: pointer;
}

.options {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
}

.options .option {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

.options .option:hover {
    background-color: #f1f1f1;
}








#title {
    display: flex;
    width: 700px;
    height: 64px;
    flex-direction: column;
    justify-content: center;
    flex-shrink: 0;

    color: #000;
    text-align: center;
    font-family: Niconne;
    font-size: 60px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}

.frame {
    border-radius: 20px 20px var(--Radius-border-radius-none, 0px) var(--Radius-border-radius-none, 0px);
    background: #121212;
    color: #FFF;
    font-family: Montserrat;
    font-size: 76px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;

    padding-left: 20px;
    padding-right: 20px;

    display: flex;
    justify-content: space-between;
    align-items: center;
}

.scene_text {
    font-size: 24px;
    padding: 10px;
}

.svo_container {
    align-items: center;
}

.svo {
    font-size: 24px;
    text-align: center;
}



.name-highlight {
    background-color: red;
}

.highlight {
    background-color: yellow;
}

.marked.character {
    /* 角色的CSS样式 */
    color: red;
    cursor: pointer;
}

.marked.action {
    /* 动作的CSS样式 */
    color: blue;
    cursor: pointer;
}

.marked.object {
    /* 物体的CSS样式 */
    color: green;
    cursor: pointer;
}

.marked.line {
    /* 对话的CSS样式 */
    color: purple;
    cursor: pointer;
}

.marked {
    font-size: 24px;
}

#legend-title {
    color: #000;
    text-align: center;
    font-family: Montserrat;
    font-size: 36px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    /* margin: 20px */
}

.legend_description {
    font-size: 24px;
    padding-left: 10px;
    padding-right: 10px;

    color: #000;
    font-family: Montserrat;
    font-size: 24px;
    font-style: italic;
    font-weight: 300;
    line-height: normal;
    position: absolute;
}

.legend_example {
    font-size: 24px;
    padding-left: 10px;
    padding-right: 10px;

    text-align: center;
    font-family: Inter;
    font-size: 24px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    position: absolute;
}

.legend_container {
    border: 2px solid #22201420;
    border-radius: 20px;
}


.grid-content {
    border: 2px solid #22201420;
    border-radius: 5px;
}

.grid-content.scenes {
    border-radius: 20px;
    border: 2px solid #ABABAB;
}


.scene_container {
    border-radius: 20px;
    border: 2px solid #ABABAB;
}

.grid-content.svo {
    border-radius: 20px;
    border: 2px solid #ABABAB;
}
</style>
