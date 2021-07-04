<template>
  <div class="main-wrapper">
    <div class="main">
      <div class="main-inner">
        <div class="page-title">
          <div class="container">
            <h1>ADD PULL REQUESTS</h1>
            <!-- /.page-title-actions -->
          </div>
          <!-- /.container-->
        </div>
        <!-- /.page-title -->
        <div class="container">
          <nav class="breadcrumb">
            <a class="breadcrumb-item" href="#">Home</a>
            <span class="breadcrumb-item active">branches</span>
          </nav>
          <div class="row mb80">
            <div class="col-sm-4 offset-sm-4">
              <h3 class="page-title-small">Login</h3>
                <form method="post" action="?">
                  <div class="form-group">
                    <label for="login-form-email">E-mail</label>
                    <input type="email" class="form-control" name="email" id="login-form-email">
                  </div>
                  <!-- /.form-group -->
                  <div class="form-group">
                    <label for="login-form-password">Password</label>
                    <input type="password" class="form-control" name="password" id="login-form-password">
                  </div>
                  <!-- /.form-group -->
                  <button type="submit" class="btn btn-primary pull-right">Login</button>
                </form>
            </div>
            <!-- /.col-sm-4 -->
          </div>
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
        name: "PullRequestAdd"
    }
</script>

<style scoped>

</style>
