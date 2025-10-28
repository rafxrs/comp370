export MAMBA_ROOT_PREFIX="/home/rreis/python/miniconda3_py313"
__mamba_setup="$("/home/rreis/python/miniconda3_py313/bin/mamba" shell hook --shell posix 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__mamba_setup"
else
    alias mamba="/home/rreis/python/miniconda3_py313/bin/mamba"  # Fallback on help from mamba activate
fi
unset __mamba_setup
