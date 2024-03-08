<template>
  <div>
    <span
      >当前日期：<a-date-picker
        v-model:value="select_data"
        :format="'YYYY/MM/DD'"
    /></span>
    <a-skeleton active :loading="ervey_loading">
      <div class="todo-list-table">
        <div class="for-item" v-for="(item, index) in todo_list" :key="index">
          <span>
            <a-switch
              v-model:checked="item.check_state"
              @change="switchChange(item)"
            >
              <template #checkedChildren><check-outlined /></template>
              <template #unCheckedChildren><close-outlined /></template>
            </a-switch>
          </span>
          <span class="item-name">&#12288;&#12288;{{ item.work_name }}</span>
        </div>
      </div>
    </a-skeleton>
  </div>
</template>
<script>
import moment from "moment";
import { getEverydayTodo, checkEverydayTodo } from "../../api/requests";
import { CheckOutlined, CloseOutlined } from "@ant-design/icons-vue";
import { message } from "ant-design-vue";
export default {
  components: {
    CheckOutlined,
    CloseOutlined,
  },
  data() {
    return {
      select_data: null,
      today_date: "",
      todo_list: [],
      ervey_loading: false,
    };
  },
  methods: {
    initEvery() {
      console.log("initEvery");
      this.ervey_loading = true;
      getEverydayTodo({
        now_user: this.$store.state.now_user,
      }).then(this.afterGetEverdayTodo);
    },
    afterGetEverdayTodo(res) {
      this.todo_list = res.data;
      this.today_date = res.today;
      this.ervey_loading = false;
    },
    switchChange(render) {
      console.log(render);
      checkEverydayTodo({
        now_user: this.$store.state.now_user,
        work_name: render.work_name,
        check_state: render.check_state,
        today: this.today_date,
      }).then(this.afterSwitchChange);
    },
    afterSwitchChange(res) {
      message.success(res.message);
    },
  },
  mounted() {
    let now = new Date();
    this.select_data = moment(
      `${now.getFullYear()}/${now.getMonth() + 1}/${now.getDate()}`
    );
  },
  created() {
    this.initEvery();
  },
  provide(){
    return {
      initEvery:this.initEvery
    }
  }
};
</script>
<style lang="scss">
.todo-list-table {
  margin: 10px 20px;
  font-size: 20px;
}
</style>