<template>
  <div>
    <a-modal
      v-model:visible="new_modal_visible"
      title="新增一个每日任务"
      @ok="handleNewTodoSubmit"
    >
      <div>
        任务名字哦：<a-input
          v-model:value="new_task_input"
          placeholder="Basic usage"
        />
      </div>
    </a-modal>

    <a-modal
      v-model:visible="fix_modal_visible"
      title="修改每日任务"
      @ok="handleFixTodoSubmit"
    >
      <div>
        任务名字哦：<a-input
          v-model:value="fix_task_input"
          placeholder="Basic usage"
        />
      </div>
    </a-modal>

    <a-button
      class="add-todo-button"
      type="primary"
      @click="new_modal_visible = true"
    >
      <template #icon><PlusOutlined /></template>
      新增任务
    </a-button>
    <a-list
      size="small"
      bordered
      :data-source="list_data"
      :loading="list_loading"
    >
      <template #renderItem="{ item }">
        <a-list-item
          >{{ item }}
          <template #actions>
            <a @click="showFixModal(item)"><EditOutlined /></a>
            <a-popconfirm
              title="真的要删除这个任务么"
              ok-text="Yes"
              cancel-text="No"
              @confirm="deleteTodoItem(item)"
            >
              <a><DeleteOutlined /></a>
            </a-popconfirm>
          </template>
        </a-list-item>
      </template>
      <template #header>
        <div><h4>设置每日打卡任务</h4></div>
      </template>
    </a-list>
  </div>
</template>
<script>
import {
  getSettingTodoList,
  createNewTodo,
  fixTodo,
  deleteTodo,
} from "../../api/requests";
import {
  PlusOutlined,
  EditOutlined,
  DeleteOutlined,
} from "@ant-design/icons-vue";
import { message } from "ant-design-vue";
export default {
  components: {
    PlusOutlined,
    EditOutlined,
    DeleteOutlined,
  },
  data() {
    return {
      list_data: [],
      list_loading: false,
      new_modal_visible: false,
      fix_modal_visible: false,
      new_task_input: "",
      fix_task_input: "",
      fix_copy_task_input: "",
    };
  },
  methods: {
    initSetting(){
      console.log('initSetting');
      this.showList();
    },
    showList() {
      this.list_loading = true;
      getSettingTodoList({ user_name: this.$store.state.now_user }).then(
        this.afterShowList
      );
    },
    afterShowList(res) {
      this.list_data = res.data.data_name;
      this.list_loading = false;
    },
    handleNewTodoSubmit() {
      createNewTodo({
        user_name: this.$store.state.now_user,
        new_todo: this.new_task_input,
      }).then(this.afterHandleNewTodoSubmit);
    },
    afterHandleNewTodoSubmit(res) {
      if (res.state == "OK") {
        this.new_modal_visible = false;
        this.new_task_input = "";
        message.success(res.message);
        this.showList();
      } else {
        message.error(res.message);
      }
    },
    handleFixTodoSubmit() {
      fixTodo({
        user_name: this.$store.state.now_user,
        new_todo: this.fix_task_input,
        old_todo: this.fix_copy_task_input,
      }).then(this.afterHandFixTOdoSubmit);
    },
    afterHandFixTOdoSubmit(res) {
      if (res.state == "OK") {
        this.fix_modal_visible = false;
        message.success(res.message);
        this.showList();
      } else {
        message.error(res.message);
      }
    },
    showFixModal(item) {
      this.fix_task_input = item;
      this.fix_copy_task_input = item;
      this.fix_modal_visible = true;
    },
    deleteTodoItem(item) {
      deleteTodo({
        user_name: this.$store.state.now_user,
        old_todo: item,
      }).then(this.afterDeleteTodoItem);
    },
    afterDeleteTodoItem(res) {
      message.success(res.message);
      this.showList();
    },
  },
  created() {
    this.initSetting()
  },
};
</script>
<style lang="scss">
.add-todo-button {
  margin: 10px 10px;
}
a-modal {
  a-input {
    margin: 5px 10px;
  }
}
</style>