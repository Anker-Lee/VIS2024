<template>
    <div id="app">
        <!-- <div id="title">{{ title }}</div> -->

        <div class="scenes" style="height: 900px; width: 700px; overflow-y: auto; overflow-x: auto; margin-top:25px;">
            <!-- v-for 创建 frame -->
            <div v-for="(scene, index) in story_info" :key="index" class="scene_container">
                <div class="frame" :class="{ frame_selected: index === currentFrameIndex }"><span
                        @click="switchFrame(scene, index)" class="frame_title">Scene {{ index + 1 }}
                    </span>
                    <!-- <button @click="toggle(index)">Toggle</button> -->
                    <el-switch v-model="toggle_rec[index]" active-color="rgba(189, 227, 255, 0.7)" inactive-color="rgba(228, 204, 255, 0.7)"
                        style="transform: scale(2); margin-right: 20px;">
                    </el-switch>
                </div>
                <!-- <div v-html="scene.text" class="scene_text" @click="handleClick" @mouseover="handleMouseover"
                    @mouseout="handleMouseleave" v-show="!toggle_rec[index]"></div> -->
                <div v-html="scene.text" class="scene_text" @click="handleClick" v-show="!toggle_rec[index]"></div>
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
                                <div class="svo" :class="{sentences: svo_object.verb === 'said'}">{{ svo_object.receiver + " " + svo_object.object }}</div>
                            </el-col>
                            <el-col :span='1'>
                                <img src="../../assets/image/arrow_top.svg"
                                    @click="toggleDesignSelector(i, scene, $event)" v-if="scene.svo_show_rec[i]"
                                    style="cursor: pointer;">
                                <img src="../../assets/image/arrow_down.svg"
                                    @click="toggleDesignSelector(i, scene, $event)" v-if="!scene.svo_show_rec[i]"
                                    style="cursor: pointer;">
                            </el-col>
                        </el-row>
                        <div v-show="scene.svo_show_rec[i]" class="action_selector" style="position: relative">
                            <!-- MOVE -->
                            <div class="action_name" style="margin-left: 25px">{{ verb2kind[svo_object.verb] }}
                            </div>
                            <el-select placeholder="Change Atomics"
                                style="position: absolute; top:5px; right: 20px; width: 200px; height: 30px;"
                                v-model="select_value"></el-select>
                            <!-- v-for 创建每个 svo list 中的设计选项 -->
                            <div v-for="(kind, j) in design_base[verb2kind[svo_object.verb]]" :key="j"
                                v-show="!showConfirmPanel[i]">
                                <!-- Hand -->
                                <div class="divider">
                                    <span class="divider-content">{{ kind["kind"] }}</span>
                                </div>
                                <div class="selection_container ">
                                    <!-- 预设的设计选项 -->
                                    <div v-for="(choice, k) in kind['choice']" :key="k" class="selection ">
                                        <!-- <img :src="require(`../../assets/image/action_figures/${verb2kind[svo_object.verb]}_${kind['kind']}_${choice}.svg`)"
                                            @click="selectDesign(scene, svo_index = i, design_selection = (verb2kind[svo_object.verb] + '_' + kind['kind'] + '_' + choice))" /> -->
                                        <img :src="require(`../../assets/image/action_figures/${verb2kind[svo_object.verb]}_${kind['kind']}_${choice}.svg`)"
                                            @click="toggleConfirmPanel(svo_index = i, args = [scene, i, (verb2kind[svo_object.verb] + '_' + kind['kind'] + '_' + choice)])"
                                            style="cursor: pointer;" />
                                        <div class="selection_name">{{ choice }}</div>
                                    </div>

                                    <!-- 自定义的设计选项 -->
                                    <div class="selection ">
                                        <img src="../../assets/image/custom.svg"
                                            style="margin: 20px 70px; cursor: pointer;" />
                                        <div class="selection_name">Custom</div>
                                    </div>
                                </div>
                            </div>

                            <div class="confirmPanel_container " v-show="showConfirmPanel[i]"
                                style="position: relative;">
                                <div class="divider">
                                    <span class="divider-content">{{ tmp_body_part }}</span>
                                </div>

                                <div class="selection" style="position: absolute; left: 20px">
                                    <img
                                        :src="require(`../../assets/image/action_figures/${tmp_kind}_${tmp_body_part}_${tmp_choice}.svg`)" />
                                    <div class="selection_name">{{ tmp_choice }}</div>
                                </div>


                                <div class="confirmPanel" style="position: absolute; right: 25px"
                                    v-if="tmp_kind === 'move'">
                                    <div style="position: absolute; left: 25px; top:10px;" class="parameter_title">
                                        Parameters</div>
                                    <div style="position: absolute; top:55px" class="param">
                                        Param #1
                                        <el-slider v-model="slider_value" range
                                            style="width: 250px; margin-left: 25px;">
                                        </el-slider>
                                    </div>
                                    <img src="../../assets/image/back.svg"
                                        style="position: absolute; right: 25px; top: 10px; cursor: pointer;"
                                        @click="backToSelection(svo_index = i)" />
                                    <button @click="selectDesign(...args)"
                                        style="position: absolute; left: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Preview</button>
                                    <button @click="confirmDesign()"
                                        style="position: absolute; right: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Apply</button>
                                </div>

                                <div class="confirmPanel" style="position: absolute; right: 25px"
                                    v-if="tmp_choice === 'dialogue box'">
                                    <div style="position: absolute; left: 25px; top:10px;" class="parameter_title">
                                        Parameters</div>

                                    <img src="../../assets/image/back.svg"
                                        style="position: absolute; right: 25px; top: 10px; cursor: pointer;"
                                        @click="backToSelection(svo_index = i)" />

                                    <div style="position: absolute; top:55px" class="param">
                                        Bubble
                                    </div>

                                    <img src="../../assets/image/Group 190speak_bubble1.svg"
                                        style="position: absolute; left: 25px; top: 100px; cursor: pointer;" />
                                    <img src="../../assets/image/Group 191.svg"
                                        style="position: absolute; right: 25px; top: 100px; cursor: pointer;" />
                                    <img src="../../assets/image/Group 194.svg"
                                        style="position: absolute; left: 25px; top: 225px; cursor: pointer;" />

                                    <div style="position: absolute; top:363px" class="param">
                                        Text Size
                                    </div>
                                    <el-select placeholder="Select"
                                        style="position: absolute; top:360px; right: 25px; width: 275px; height: 25px;"
                                        v-model="select_value">
                                        <el-option v-for="item in font_size_options" :key="item.value"
                                            :label="item.label" :value="item.value">
                                        </el-option>
                                    </el-select>

                                    <div style="position: absolute; top:438px" class="param">
                                        Content
                                    </div>
                                    <input type="text" style="position: absolute; bottom: 100px; right: 25px; width: 258px; height: 90px; padding-left: 12px; color: #A8ABB2; border-radius: var(--Radius-border-radius-base, 4px);
                                    border: 1px solid var(--Color-Text-text-color-disabled, #C0C4CC);
                                    background: var(--Color-Fill-fill-color-blank, #FFF);" placeholder="Enter" />


                                    <button @click="selectDesign(...args)"
                                        style="position: absolute; left: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Preview</button>
                                    <button @click="confirmDesign()"
                                        style="position: absolute; right: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Apply</button>
                                </div>

                                <div class="confirmPanel" style="position: absolute; right: 25px"
                                    v-if="tmp_choice === 'thought bubble'">
                                    <div style="position: absolute; left: 25px; top:10px;" class="parameter_title">
                                        Parameters</div>
                                    <img src="../../assets/image/back.svg"
                                        style="position: absolute; right: 25px; top: 10px; cursor: pointer;"
                                        @click="backToSelection(svo_index = i)" />
                                    <div style="position: absolute; top:55px" class="param">
                                        Bubble
                                    </div>
                                    <img src="../../assets/image/Group 192.svg"
                                        style="position: absolute; left: 25px; top: 100px; cursor: pointer;" />
                                    <img src="../../assets/image/Group 193.svg"
                                        style="position: absolute; right: 25px; top: 100px; cursor: pointer;" />
                                    <div style="position: absolute; top:363px" class="param">
                                        Text Size
                                    </div>
                                    <el-select placeholder="Select"
                                        style="position: absolute; top:360px; right: 25px; width: 275px; height: 25px;"
                                        v-model="select_value"></el-select>
                                    <div style="position: absolute; top:438px" class="param">
                                        Content
                                    </div>
                                    <input type="text" style="position: absolute; bottom: 100px; right: 25px; width: 258px; height: 90px; padding-left: 12px; color: #A8ABB2; border-radius: var(--Radius-border-radius-base, 4px);
                                    border: 1px solid var(--Color-Text-text-color-disabled, #C0C4CC);
                                    background: var(--Color-Fill-fill-color-blank, #FFF);" placeholder="Enter" />
                                    <button @click="selectDesign(...args)"
                                        style="position: absolute; left: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Preview</button>
                                    <button @click="confirmDesign()"
                                        style="position: absolute; right: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Apply</button>
                                </div>

                                <div class="confirmPanel" style="position: absolute; right: 25px"
                                    v-if="tmp_choice === 'direct'">
                                    <div style="position: absolute; left: 25px; top:10px;" class="parameter_title">
                                        Parameters</div>
                                    <img src="../../assets/image/back.svg"
                                        style="position: absolute; right: 25px; top: 10px; cursor: pointer;"
                                        @click="backToSelection(svo_index = i)" />

                                    <div style="position: absolute; top:55px" class="param">
                                        Font
                                    </div>
                                    <el-select placeholder="Select"
                                        style="position: absolute; top:55px; right: 25px; width: 275px; height: 25px;"
                                        v-model="select_value"></el-select>

                                    <div style="position: absolute; top:113px" class="param">
                                        Text Size
                                    </div>
                                    <el-select placeholder="Select"
                                        style="position: absolute; top:113px; right: 25px; width: 275px; height: 25px;"
                                        v-model="select_value"></el-select>

                                    <div style="position: absolute; top:220px" class="param">
                                        Content
                                    </div>
                                    <input type="text" style="position: absolute; top: 188px; right: 25px; width: 258px; height: 90px; padding-left: 12px; color: #A8ABB2; border-radius: var(--Radius-border-radius-base, 4px);
                                    border: 1px solid var(--Color-Text-text-color-disabled, #C0C4CC);
                                    background: var(--Color-Fill-fill-color-blank, #FFF);" placeholder="Enter" />

                                    <button
                                        style="position: absolute; right: 25px; top: 305px; cursor: pointer; width: 175px; height: 75px;"
                                        class="parameter_button">Position Adjusting</button>

                                    <button @click="selectDesign(...args)"
                                        style="position: absolute; left: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Preview</button>
                                    <button @click="confirmDesign()"
                                        style="position: absolute; right: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Apply</button>
                                </div>


                                <div class="confirmPanel" style="position: absolute; right: 25px"
                                    v-if="tmp_choice === 'path'">
                                    <div style="position: absolute; left: 25px; top:10px;" class="parameter_title">
                                        Parameters</div>
                                    <img src="../../assets/image/back.svg"
                                        style="position: absolute; right: 25px; top: 10px; cursor: pointer;"
                                        @click="backToSelection(svo_index = i)" />

                                    <div style="position: absolute; top:55px" class="param">
                                        Speed
                                    </div>
                                    <el-slider v-model="slider_value" range
                                        style="width: 250px; position: absolute; top: 55px; right: 25px;">
                                    </el-slider>


                                    <button
                                        style="position: absolute; right: 25px; top: 120px; cursor: pointer; width: 175px; height: 75px;"
                                        class="parameter_button">Path Setting</button>
                                    <button @click="selectDesign(...args)"
                                        style="position: absolute; left: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Preview</button>
                                    <button @click="confirmDesign()"
                                        style="position: absolute; right: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Apply</button>
                                </div>

                                <div class="confirmPanel" style="position: absolute; right: 25px"
                                    v-if="tmp_kind === 'propel'">
                                    <div style="position: absolute; left: 25px; top:10px;" class="parameter_title">
                                        Parameters</div>
                                    <img src="../../assets/image/back.svg"
                                        style="position: absolute; right: 25px; top: 10px; cursor: pointer;"
                                        @click="backToSelection(svo_index = i)" />

                                    <div style="position: absolute; top:55px" class="param">
                                        Speed
                                    </div>
                                    <el-slider v-model="slider_value" 
                                        style="width: 250px; position: absolute; top: 55px; right: 25px;">
                                    </el-slider>


                                    <button
                                        style="position: absolute; right: 25px; top: 120px; cursor: pointer; width: 175px; height: 75px;"
                                        class="parameter_button">Path Setting</button>
                                    <button @click="selectDesign(...args)"
                                        style="position: absolute; left: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Preview</button>
                                    <button @click="confirmDesign()"
                                        style="position: absolute; right: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Apply</button>
                                </div>

                                <div class="confirmPanel" style="position: absolute; right: 25px"
                                    v-if="tmp_kind === 'expel'">
                                    <div style="position: absolute; left: 25px; top:10px;" class="parameter_title">
                                        Parameters</div>
                                    <img src="../../assets/image/back.svg"
                                        style="position: absolute; right: 25px; top: 10px; cursor: pointer;"
                                        @click="backToSelection(svo_index = i)" />

                                    <div style="position: absolute; top:55px" class="param">
                                        Speed
                                    </div>
                                    <el-slider v-model="slider_value" 
                                        style="width: 250px; position: absolute; top: 55px; right: 25px;">
                                    </el-slider>


                                    <button
                                        style="position: absolute; right: 25px; top: 120px; cursor: pointer; width: 175px; height: 75px;"
                                        class="parameter_button">Path Setting</button>
                                    <button @click="selectDesign(...args)"
                                        style="position: absolute; left: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Preview</button>
                                    <button @click="confirmDesign()"
                                        style="position: absolute; right: 25px; bottom: 25px; cursor: pointer;"
                                        class="parameter_button">Apply</button>
                                </div>

                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="legend_container" style="position: relative; height: 200px; margin-top: 30px;">
            <div id="legend-title" style="margin-top: 20px;">Legend</div>
            <span class="legend_example"
                style="background-color:rgba(242, 72, 34, 0.5); left: 50px; top: 90px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="legend_description" style="left: 130px; top: 90px;">Character</span>

            <span class="legend_example right"
                style="background-color:rgba(20, 174, 92, 0.5); left: 470px; top: 90px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="legend_description right" style="left:550px; top: 90px;">Item</span>

            <span class="legend_example"
                style="background-color:rgba(255, 205, 41, 0.3); left: 50px; top: 140px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="legend_description" style="left: 130px; top: 140px;">Thought & Dialogue</span>

            <span class="legend_example right"
                style="background-color:rgba(13, 153, 255, 0.5); left: 470px; top: 140px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="legend_description right" style="left:550px; top: 140px;">Action</span>
        </div>

    </div>
</template>

<script>
export default {
    data() {
        return {
            font_size_options: [
                // 10， 12， 14， 16， 20， 24， 28， 32， 36， 40
                {
                    value: '10', // 字体大小
                    label: '10'
                },
                {
                    value: '12',
                    label: '12'
                },
                {
                    value: '14',
                    label: '14'
                },
                {
                    value: '16',
                    label: '16'
                },
                {
                    value: '20',
                    label: '20'
                },
                {
                    value: '24',
                    label: '24'
                },
                {
                    value: '28',
                    label: '28'
                },
                {
                    value: '32',
                    label: '32'
                },
                {
                    value: '36',
                    label: '36'
                },
                {
                    value: '40',
                    label: '40'
                }
            ],
            select_value: null,
            title: "Little Red Riding Hood",
            hoveredIndex: null,
            story_info: [],
            toggle_rec: {},
            showSelector: false, // 是否显示设计选择器
            design_selector_data: {},
            verb2kind: {
                "said": "speak",
                "gave": 'atrans',
                'opened': 'propel',
                'cry': 'expel',
                'went': 'ptrans',
                'thought': 'mental',
                'kicked': 'move',
                'rotated': 'move',
                'raised': 'propel',
                'pulled': 'propel',
                'changed': 'expel',
                'pushed': 'propel'
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
                    },
                    {
                        'kind': 'all',
                        'choice': ['rotate']
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
            showConfirmPanel: [],
            showConfirm_atrans_all_disappear: false,
            showConfirm_atrans_all_path: false,
            showConfirm_expel_all_appear: false,
            showConfirm_expel_all_appear_path: false,
            showConfirm_ingest_all_disappear: false,
            showConfirm_ingest_all_path_disappear: false,
            showConfirm_mental_all_thought_bubble: false,
            showConfirm_move_feet_drub: false,
            showConfirm_move_feet_kick: false,
            showConfirm_move_feet_raise: false,
            showConfirm_move_feet_walk: false,
            showConfirm_move_hand_raise: false,
            showConfirm_move_hand_wave: false,
            showConfirm_move_head_nod: false,
            showConfirm_move_head_shake: false,
            showConfirm_propel_all_grasp: false,
            showConfirm_propel_all_kick: false,
            showConfirm_propel_all_pull: false,
            showConfirm_propel_all_push: false,
            showConfirm_propel_all_throw: false,
            showConfirm_ptrans_all_dis_reappear: false,
            showConfirm_ptrans_all_path: false,
            showConfirm_speak_all_dialogue_box: false,
            showConfirm_speak_all_direct: false,
            args: [],
            selected_design: null,
            slider_value: [20, 50],
            currentFrameIndex: -1,
            tmp_kind: 'ptrans',
            tmp_body_part: 'all',
            tmp_choice: 'path'
        };
    },
    computed: {
        notShowSelectionPanel: function () {
            return this.showConfirm_atrans_all_disappear || this.showConfirm_atrans_all_path || this.showConfirm_expel_all_appear || this.showConfirm_expel_all_appear_path || this.showConfirm_ingest_all_disappear || this.showConfirm_ingest_all_path_disappear || this.showConfirm_mental_all_thought_bubble || this.showConfirm_move_feet_drub || this.showConfirm_move_feet_kick || this.showConfirm_move_feet_raise || this.showConfirm_move_feet_walk || this.showConfirm_move_hand_raise || this.showConfirm_move_hand_wave || this.showConfirm_move_head_nod || this.showConfirm_move_head_shake || this.showConfirm_propel_all_grasp || this.showConfirm_propel_all_kick || this.showConfirm_propel_all_pull || this.showConfirm_propel_all_push || this.showConfirm_propel_all_throw || this.showConfirm_ptrans_all_dis_reappear || this.showConfirm_ptrans_all_path || this.showConfirm_speak_all_dialogue_box || this.showConfirm_speak_all_direct;
        }
    },
    watch: {
        story_info: {
            handler: function (val) {
                this.$bus.$emit("initialize", val);
                console.log('emit initialize');
            },
            deep: false
        }
    },
    mounted() {
        this.$bus.$on("pass_story_info", (story_info) => {
            story_info.forEach((scene, j) => {
                let svo_show_rec = {}
                scene.svo.forEach((_, index) => {
                    svo_show_rec[index] = false;
                });
                scene['svo_show_rec'] = svo_show_rec;

                this.$set(this.showConfirmPanel, j, false);
            });
            this.story_info = story_info;
            console.log("初始化, 载入 story_info: ", this.story_info);
        })
    },
    methods: {
        confirmDesign() {
            console.log("confirmDesign");
            this.$bus.$emit("confirm_design");
        },
        backToSelection(svo_index) {
            this.$set(this.showConfirmPanel, svo_index, false);
            this.$bus.$emit("clear_user_design_cache");
        },
        toggleConfirmPanel(svo_index, args) {
            console.log("args", args);
            this.$set(this.showConfirmPanel, svo_index, !this.showConfirmPanel[svo_index]);
            this.args = args;
            this.selected_design = args[2];
            this.tmp_kind = args[2].split('_')[0];
            this.tmp_body_part = args[2].split('_')[1];
            this.tmp_choice = args[2].split('_')[2];

            console.log("tmp_kind", this.tmp_kind, "tmp_body_part", this.tmp_body_part, "tmp_choice", this.tmp_choice);
        },
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

        // selectOption(option) {
        //     // this.selectedOption = option;
        //     this.showOptions = false;
        // },
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
            Object.keys(scene['svo_show_rec']).forEach((key) => {
                if (key !== i.toString()) {
                    this.$set(scene['svo_show_rec'], key, false);
                } else if (key === i.toString()) {
                    this.$set(scene['svo_show_rec'], key, !(scene['svo_show_rec'][key]));
                }
            });
            // this.$set(scene['svo_show_rec'], i, !(scene['svo_show_rec'][i]))
        },
        switchFrame(scene, index) {
            console.log("切换到Frame:", index);
            this.$bus.$emit("switch_frame", [scene, index]);
            this.currentFrameIndex = index;
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
    background: #B2AAD1;


    padding-left: 20px;
    padding-right: 20px;

    display: flex;
    justify-content: space-between;
    align-items: center;
}

.frame_selected {
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
    font-size: 20px;
    font-style: normal;
    font-weight: 500;
    line-height: 22px;
    text-transform: uppercase;
    /* 55% */
}


.marked.character {
    background-color: rgba(242, 72, 34, 0.5);
}

.marked.action {
    background-color: rgba(13, 153, 255, 0.5);
}

.marked.object {
    background-color: rgba(20, 174, 92, 0.5);
}

.marked.line {
    background-color: rgba(255, 205, 41, 0.3);
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
    margin-bottom: 10px;
}

.scene_container:last-child {
    margin-bottom: 0px;
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

.confirmPanel {
    width: 425px;
    height: 600px;
    flex-shrink: 0;

    border-radius: 10px;
    border: 2px solid #5E4F94;
    background: #FFFCF9;
}

.confirmPanel_container {
    width: 700px;
    height: 670px;
    flex-shrink: 0;
}

.parameter_title {
    display: flex;
    align-items: center;
    justify-content: center;

    color: var(--color-black, #000);
    font-family: Montserrat;
    font-size: 24px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    text-align: center;
}

.parameter_button {
    width: 175px;
    height: 50px;

    color: var(--color-black, #000);
    text-align: center;
    font-family: Montserrat;
    font-size: 20px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;

    border-radius: 10px;
    border: 1px solid #5E4F94;
    background: #FFFCF9;

    display: flex;
    justify-content: center;
    align-items: center;
}

.param {
    color: var(--color-black, #000);
    font-family: Montserrat;
    font-size: 20px;
    font-style: italic;
    font-weight: 400;
    line-height: normal;

    width: 600px;

    display: flex;
    align-items: center;
    margin-left: 25px;
}

.sentences {
    color: var(--color-black, #000);
    text-align: center;
    font-family: Inter;
    font-size: 20px;
    font-style: italic;
    font-weight: 500;
    line-height: 22px;
}
</style>
