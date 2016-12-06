def __set_defaults_marvell_embedded_linux_yocto():
    import os
    import sys

    valid_machines = [
        'clearfog',
        'db-88f6820-amc',
        'db-88f6820-gp',
        'db-88f7040-modular',
        'db-88f3720-ddr3-modular',
        'db-88f8040-modular',
    ]

    local_conf_exists = os.path.isfile(os.path.join(build_dir,
                                                    'conf',
                                                    'local.conf'))

    def required_var_error(varname, valid_vals):
        sys.stderr.write("ERROR: You must set '%s' before setting up the environment.\n" %
                         (varname,))
        sys.stderr.write("       Set MACHINE variable with one of the possible values.\n"
                         "       Possible values are: %s\n\n"
                         "       Ex: MACHINE=clearfog source setup-environment build\n"
                         % valid_vals)
        sys.exit(1)

    def maybe_set_default(varname, valid_vals):
        try:
            val = os.environ[varname]
        except KeyError:
            val = None

        if val:
            if val in valid_vals:
                set_default(varname, val)
            else:
                required_var_error(varname, valid_vals)
        elif not local_conf_exists:
            required_var_error(varname, valid_vals)

    maybe_set_default('MACHINE', valid_machines)
    set_default('DISTRO', 'marvell')

def __after_init_marvell_embedded_linux_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']

    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                     'meta-openembedded/meta-python',
                     'meta-openembedded/meta-oe',
                     'meta-openembedded/meta-networking',
                     'meta-openembedded/meta-filesystems',
                     'meta-marvell-distro',
                     'meta-marvell',
                     'meta-virtualization'
                    ]])


run_set_defaults(__set_defaults_marvell_embedded_linux_yocto)
run_after_init(__after_init_marvell_embedded_linux_yocto)
