import os

# params: (vars) list of environment variables as strings
def get_env_vars(vars):
	r = {}
	for var in vars:
		r[var] = os.getenv(var)
	return r

# --------------------- test ---------------------

print(get_env_vars(["_Cookie","_domain","_ElevenSquared","_SystemId","_Test","_USER"]))

input()