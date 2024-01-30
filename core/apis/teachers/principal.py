from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from .schema import TeacherSchema
teacher_principal_resources = Blueprint('teacher_principal_resources', __name__)


@teacher_principal_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """List all the teachers"""
    teachers = Teacher.get_all_teachers()
    teacher_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teacher_dump)



