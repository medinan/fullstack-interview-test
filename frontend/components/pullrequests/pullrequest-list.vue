<template>
  <div class="main-wrapper">
    <div class="main">
      <div class="main-inner">
        <div class="page-title">
          <div class="container">
            <h1>PULL REQUESTS</h1>
            <!-- /.page-title-actions -->
          </div>
          <!-- /.container-->
        </div>
        <!-- /.page-title -->
        <div class="container">
          <nav class="breadcrumb">
            <a class="breadcrumb-item" href="/">Home</a>
            <span class="breadcrumb-item active">branches</span>
          </nav>
          <a href="/pullrequests/add/">
            <button type="button" class="btn btn-success pull-right">New pull request</button>
          </a>

          <table class="table">
            <thead>
            <tr>
              <th scope="col">Author</th>
              <th scope="col">Title</th>
              <th scope="col">Description</th>
              <th scope="col">Status</th>
            </tr>
            </thead>
            <tbody>
              <tr v-for="(pull, index) in pullrequests">
                <td>{{pull.author}}</td>
                <td>{{pull.title}}</td>
                <td>{{pull.description}}</td>
                <td>{{pull.status}}</td>
                <td><button v-on:click="closePullRequest(index)" class="btn btn-primary pull-right" v-if="pull.status === 'open'">closed</button></td>
              </tr>

            </tbody>
          </table>
          <!-- /.row -->
        </div>
        <!-- /.container-fluid -->
      </div>
      <!-- /.main-inner -->
    </div>
    <!-- /.main -->
  </div>
</template>

<script>

  export default {
    name: "PullRequestList",
    mounted: function () {
      this.getPullRequests();
    },
    data: function () {
      return {
        pullrequests: []
      }
    },
    methods: {
      getPullRequests: function () {
        const url = "/api/v1/pullrequests/"
        let self = this;
        this.$axios.get(url, {
          dataType: "json",
          headers: {"Content-type": "application/json"}
        }).then(function (response) {
          self.pullrequests = response.data;
        })
      },
      closePullRequest: function (index) {
        const url = "/api/v1/pullrequests/" + item.pk + "/close/"
        let self = this;
        this.$axios.put(url, {
          dataType: "json",
          headers: {"Content-type": "application/json"}
        }).then(function (response) {
          self.getPullRequests();
        })
      }
    }
  }
</script>

<style scoped>

</style>
