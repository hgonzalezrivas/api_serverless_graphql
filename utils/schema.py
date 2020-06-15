import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from utils.models import Department as DepartmentModel
from utils.models import Employee as EmployeeModel
from utils.models import Role as RoleModel
from utils.models import FranquiciaDashboard as FranquiciaModel

class Department(MongoengineObjectType):

    class Meta:
        model = DepartmentModel
        interfaces = (Node,)

class Role(MongoengineObjectType):

    class Meta:
        model = RoleModel
        interfaces = (Node,)

class Employee(MongoengineObjectType):

    class Meta:
        model = EmployeeModel
        interfaces = (Node,)


class Franquicia(MongoengineObjectType):

    class Meta:
        model = FranquiciaModel
        interfaces = (Node,)

class createEmployee(graphene.Mutation):
    class Input:
        name = graphene.String()
    ok = graphene.Boolean()
    employee = graphene.Field(Employee)

    @classmethod
    def mutate(cls, _, args, **kwargs):
        employee = EmployeeModel(name=kwargs.get('name'), department=kwargs.get('department'), role=kwargs.get('role'))
        employee.save()
        ok = True
        return createEmployee(employee)



class Query(graphene.ObjectType):
    node = Node.Field()
    all_employess = MongoengineConnectionField(Employee)
    all_role = MongoengineConnectionField(Role)
    all_dashboard = MongoengineConnectionField(Franquicia)
    role = graphene.Field(Role)

class Mutations(graphene.ObjectType):
    create_employee = createEmployee.Field()

schema = graphene.Schema(query= Query, mutation=Mutations, types=[Department, Employee, Role, Franquicia])