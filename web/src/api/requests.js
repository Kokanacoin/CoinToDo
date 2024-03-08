import http from "../utils/axios";

// export const testApi = data => {
//   return http({
//     url: "/api/todo/test_api",//接口
//     method: "post",
//     data: data
//   });
// };
export const testApi = (param)=> {
  return http({
    url: "/todo/test_api/",//接口
    method: "get",
    params: {
      t: param
    },
  });
};

export const getUserList = (param)=> {
  return http({
    url: "/todo/getUserList/",//接口
    method: "post",
    data: param
  });
};

export const getSettingTodoList = (param)=> {
  return http({
    url: "/todo/getSettingTodoList/",//接口
    method: "post",
    data: param
  });
};
export const createNewTodo = (param)=> {
  return http({
    url: "/todo/createNewTodo/",//接口
    method: "post",
    data: param
  });
};
export const fixTodo = (param)=> {
  return http({
    url: "/todo/fixTodo/",//接口
    method: "post",
    data: param
  });
};

export const deleteTodo = (param)=> {
  return http({
    url: "/todo/deleteTodo/",//接口
    method: "post",
    data: param
  });
};

export const getEverydayTodo = (param)=> {
  return http({
    url: "/todo/getEverydayTodo/",//接口
    method: "post",
    data: param
  });
};

export const checkEverydayTodo = (param)=> {
  return http({
    url: "/todo/checkEverydayTodo/",//接口
    method: "post",
    data: param
  });
};

export const getStatisticData = (param)=> {
  return http({
    url: "/todo/getStatisticData/",//接口
    method: "post",
    data: param
  });
};











