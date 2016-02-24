def __after_init_embedded_linux_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']

    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                     'meta-openembedded/meta-python',
                     'meta-openembedded/meta-oe',
                     'meta-openembedded/meta-networking',
                     'meta-openembedded/meta-filesystems',
                     'meta-marvell-distro',
                     'meta-marvell'
                    ]])



run_after_init(__after_init_embedded_linux_yocto)
