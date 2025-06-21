from controllers.user_controllers import Register, Login, Tasks

def register_user_routes(api):
    api.add_resource(Register, '/user/register')
    api.add_resource(Login, '/user/login')
    api.add_resource(Tasks, '/user/tasks')
