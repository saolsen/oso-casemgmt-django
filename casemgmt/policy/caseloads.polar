## Model-specific rules for caseload roles.
## (Would be autogenerated by oso)

# User in caseload role (directly) or User in caseload role (as a group member)
user_in_role(user: casemgmt::User, role, resource: casemgmt::Caseload) if
    ## Note: we are using the related name to go from resource to the m2m model
    ## This should be preferred so all attributes at written over the resource partial
    caseload_role in resource.caseload_roles and
    role = caseload_role.role and
    (caseload_role.user = user or
     user in caseload_role.group.user);
