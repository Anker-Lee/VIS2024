<template>
    <div id="app">
        <div id="title">{{ title }}</div>

        <div class="scenes" style="height: 860px; width: 700px; overflow-y: auto; overflow-x: auto;">
            <!-- v-for 创建 frame -->
            <div v-for="(scene, index) in story_info" :key="index" class="scene_container">
                <div class="frame"><span @click="switchFrame(scene, index)" class="frame_title">Frame {{ index + 1 }}
                    </span>
                    <!-- <button @click="toggle(index)">Toggle</button> -->
                    <el-switch v-model="toggle_rec[index]" active-color="#13ce66" inactive-color="#ff4949"
                        style="transform: scale(2); margin-right: 20px;">
                    </el-switch>
                </div>
                <div v-html="scene.text" class="scene_text" @click="handleClick" @mouseover="handleMouseover"
                    @mouseout="handleMouseleave" v-show="!toggle_rec[index]"></div>
                <div v-show="toggle_rec[index]">
                    <!-- v-for 创建每个frame中的 svo list -->
                    <div v-for="(svo_object, i) in scene.svo" :key="i" class="svo_container">
                        <!-- e 是一个 svo 对象 {subject: , verb: , object: } -->
                        <el-row :gutter="10" style="display:flex; align-items: center; padding: 20px 40px;">
                            <el-col :span="5">
                                <div class="svo">{{ svo_object.subject }}</div>
                            </el-col>
                            <el-col :span="5">
                                <div class="svo svo_verb">{{ svo_object.verb }}</div>
                            </el-col>
                            <el-col :span="13">
                                <div class="svo">{{ svo_object.object }}</div>
                            </el-col>
                            <el-col :span='1'>
                                <img src="../../assets/image/ArrowRightBold.svg"
                                    @click="toggleDesignSelector(i, scene, $event)">
                            </el-col>
                        </el-row>
                        <div v-show="scene.svo_show_rec[i]" class="action_selector">
                            <div class="action_name" style="margin-left: 25px">{{ verb2kind[svo_object.verb] }}
                            </div>
                            <!-- v-for 创建每个 svo list 中的设计选项 -->
                            <div v-for="(kind, j) in design_base[verb2kind[svo_object.verb]]" :key="j">
                                <div class="divider" v-if="kind['kind'] !== 'all'">
                                    <span class="divider-content">{{ kind["kind"] }}</span>
                                </div>
                                <div class="selection_container ">
                                    <!-- 预设的设计选项 -->
                                    <div v-for="(choice, k) in kind['choice']" :key="k" @click="selectOption(choice)"
                                        class="selection ">
                                        <img :src="require(`../../assets/image/action_figures/${verb2kind[svo_object.verb]}_${kind['kind']}_${choice}.svg`)"
                                            @click="selectDesign(scene, svo_index = i, design_selection = (verb2kind[svo_object.verb] + '_' + kind['kind'] + '_' + choice))" />
                                        <!-- <img src="../../assets/image/action_figures/move_head_nod.svg" /> -->
                                        <div class="selection_name">{{ choice }}</div>
                                    </div>

                                    <!-- 自定义的设计选项 -->
                                    <div class="selection ">
                                        <img src="../../assets/image/custom.svg" style="margin: 20px 70px;" />
                                        <div class="selection_name">Custom</div>
                                    </div>
                                </div>

                                <div class="" v-show="">
                                    <button>Back</button>
                                    <button>Preview</button>
                                    <button>Confirm</button>
                                </div>


                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="legend_container" style="position: relative; height: 200px; margin-top: 30px;">
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
            showSelector: false, // 是否显示设计选择器
            design_selector_data: {},
            verb2kind: {
                "said": "speak",
                "gave": 'atrans',
                'opened': 'move',
                'cry': 'expel',
                'went': 'ptrans',
                'thought': 'mental',
                'kicked': 'move',
            },
            design_base: {
                "move": [
                    {
                        'kind': 'head',
                        'choice': ['shake', 'nod']
                    },
                    {
                        'kind': 'hand',
                        'choice': ['raise', 'wave']
                    },
                    {
                        'kind': 'feet',
                        'choice': ['kick', 'raise', 'drub', 'walk']
                    }
                ],
                "ptrans": [
                    {
                        'kind': 'all',
                        'choice': ['path', 'dis-reappear']
                    }
                ],
                "atrans": [
                    {
                        'kind': 'all',
                        'choice': ['path', 'dis-reappear']
                    }
                ],
                "ingest": [
                    {
                        'kind': 'all',
                        'choice': ['path-disappear', 'disappear']
                    }
                ],
                "expel": [
                    {
                        'kind': 'all',
                        'choice': ['appear-path', 'appear']
                    }
                ],
                "speak": [
                    {
                        'kind': 'all',
                        'choice': ['dialogue box', 'direct']
                    }
                ],
                "mental": [
                    {
                        'kind': 'all',
                        'choice': ['thought bubble']
                    }
                ],
                "propel": [
                    {
                        'kind': 'all',
                        'choice': ['push', 'pull', 'throw', 'kick', 'grasp']
                    }
                ]
            },
        };
    },
    watch: {
        story_info: {
            handler: function (val) {
                this.$bus.$emit("initialize", val);
            },
            deep: false
        }
    },
    mounted() {
        this.$bus.$on("pass_story_info", (story_info) => {
            story_info.forEach((scene) => {
                let svo_show_rec = {}
                scene.svo.forEach((_, index) => {
                    svo_show_rec[index] = false;
                });
                scene['svo_show_rec'] = svo_show_rec;
            });
            this.story_info = story_info;
            console.log("story_info: ", this.story_info);
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
                // console.log('mouse over:', event.target);
                event.target.style.backgroundColor = "yellow";
            }
        },
        handleMouseleave(event) {
            if (event.target.classList.contains('marked')) {
                // console.log('mouse leave:', event.target);
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
        // toggleDesignSelector(svo_object, event) { // 切换是否显示设计选择器
        //     console.log(svo_object);
        //     if (this.showSelector === false) {
        //         this.design_selector_data = svo_object;

        //         const button = event.target;

        //         const design_selector = document.getElementById('design_selector');
        //         design_selector.style.left = button.getBoundingClientRect().right - 40 + 'px';
        //         design_selector.style.top = button.getBoundingClientRect().top -80 + 'px';

        //         this.showSelector = true;
        //     } else if (this.showSelector === true) {
        //         if (this.design_selector_data === svo_object) {
        //             this.showSelector = false;
        //             this.design_selector_data = {};
        //         } else {
        //             this.design_selector_data = svo_object;

        //             const button = event.target;

        //             const design_selector = document.getElementById('design_selector');
        //             design_selector.style.left = button.getBoundingClientRect().right - 40+ 'px';
        //             design_selector.style.top = button.getBoundingClientRect().top - 80 + 'px';
        //         }
        //     }
        // },
        toggleDesignSelector(i, scene) { // 切换是否显示设计选择器
            this.$set(scene['svo_show_rec'], i, !(scene['svo_show_rec'][i]))
        },
        switchFrame(scene, index) {
            console.log("切换到Frame:", index);
            this.$bus.$emit("switch_frame", [scene, index]);
        },
        selectDesign(scene, svo_index, design_selection) {
            console.log(scene, svo_index, design_selection);
            this.$bus.$emit("select_design", {
                scene: scene,
                svo_index: svo_index,
                design_selection: design_selection
            });
        }
    },
};
</script>

<style>
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
    background: #7566A9;


    padding-left: 20px;
    padding-right: 20px;

    display: flex;
    justify-content: space-between;
    align-items: center;
}

.frame_title {
    color: #FFF;
    font-family: Montserrat;
    font-size: 76px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    cursor: pointer;
}

.scene_text {
    padding: 10px;

    color: var(--color-black, #000);
    font-family: Inter;
    font-size: 24px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}

.svo_container {
    align-items: center;
    border-radius: 20px;
    border: 2px solid #B2AAD1;
}

.svo {
    color: var(--color-black, #000);
    text-align: center;
    font-family: Inter;
    font-size: 20px;
    font-style: normal;
    font-weight: 500;
    line-height: 22px;
    /* 68.75% */
}

.svo_verb {
    color: var(--color-black, #000);
    text-align: center;
    font-family: Inter;
    font-size: 40px;
    font-style: normal;
    font-weight: 700;
    line-height: 22px;
    text-transform: uppercase;
    /* 55% */
}


.name-highlight {
    background-color: red;
}

.highlight {
    background-color: yellow;
}

.marked.character {
    /* 角色的CSS样式 */
    /* color: white; */
    border-radius: 1em 0 1em 0;
    background-image: linear-gradient(-100deg,
            rgba(255, 20, 0, 0.2),
            rgba(255, 20, 0, 0.7) 95%,
            rgba(255, 20, 0, 0.1));
    cursor: pointer;
}

.marked.action {
    /* 动作的CSS样式 */
    /* color: white;
    background-color: blue; */
    border-radius: 1em 0 1em 0;
    background-image: linear-gradient(-100deg,
            rgba(0, 20, 255, 0.2),
            rgba(0, 20, 255, 0.7) 95%,
            rgba(0, 20, 255, 0.1));
    cursor: pointer;
}

.marked.object {
    /* 物体的CSS样式 */
    /* color: white; */
    border-radius: 1em 0 1em 0;
    background-image: linear-gradient(-100deg,
            rgba(0, 255, 20, 0.2),
            rgba(0, 255, 20, 0.7) 95%,
            rgba(0, 255, 20, 0.1));
    cursor: pointer;
}

.marked.line {
    /* 对话的CSS样式 */
    /* color: white; */
    border-radius: 1em 0 1em 0;
    background-image: linear-gradient(-100deg,
            rgba(255, 224, 0, 0.2),
            rgba(255, 224, 0, 0.7) 95%,
            rgba(255, 224, 0, 0.1));
    cursor: pointer;
}

.marked {
    font-size: 24px;
}

.scenes {
    border-top: 2px solid #B2AAD1;
    border-bottom: 2px solid #B2AAD1;
    border-radius: 20px;
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
    width: 700px;
    height: 200px;
    border-radius: 0px 0px 20px 20px;
    border: 2px solid #B2AAD1;
}

.grid-content {
    border: 2px solid #22201420;
    border-radius: 5px;
}


.scene_container {
    border-radius: 20px;
    border: 2px solid #ABABAB;
}

.grid-content.svo {
    border-radius: 20px;
    border: 2px solid #ABABAB;
}

#design_selector {
    position: absolute;
    width: 400px;
    z-index: 100;
    border: 2px solid #000;
}

.action_selector {
    /* width: 700px; */
    flex-shrink: 0;

    border-radius: 0px 0px 20px 20px;
    border-top: 2px solid #B2AAD1;
    background: #FFF;
}

.action_name {
    height: 50px;

    color: var(--color-black, #000);
    font-family: Montserrat;
    font-size: 38px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    text-transform: uppercase;

    display: flex;
    align-items: center;
}

.selection_container {
    display: grid;
    grid-template-columns: repeat(auto-fill, 200px);
    grid-gap: 0px 25px;
    justify-content: space-between;
    width: 650px;
    margin: 0px 20px;
}

.selection {
    width: 200px;
    height: 150px;
}

.selection_name {
    width: 200px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;

    color: var(--color-black, #000);
    text-align: center;
    font-family: Inter;
    font-size: 24px;
    font-style: italic;
    font-weight: 400;
    line-height: normal;
    text-transform: capitalize;
}

.divider {
    display: flex;
    align-items: center;
    text-align: center;
    margin: 10px 20px;
}

.divider::before {
    content: '';
    flex: 0.1;
    /* 调整这个值来控制虚线的长度 */
    border-bottom: 2px dashed #000;
    margin-right: .5em;
}

.divider::after {
    content: '';
    flex: 1.9;
    /* 调整这个值来控制虚线的长度 */
    border-bottom: 2px dashed #000;
    margin-left: .5em;
}

.divider-content {
    padding: 0 10px;
    color: var(--color-black, #000);
    font-family: Montserrat;
    font-size: 32px;
    font-style: italic;
    font-weight: 400;
    line-height: normal;
    text-transform: capitalize;
    /* 设置文本位置 */
}
</style>
