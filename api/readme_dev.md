# Sample running tools:

Run doc gen (html2 template)

```
abandonned:
$ openapi-generator generate -i myphr_api.swagger -g html2 -o tmpout
```
 Generate code via the following command while in the right directory:
 $ openapi-generator generate -i ./myphr_api.swagger -g python-flask -o ./impl_tmp
 then
 $ rsync -va ./impl_tmp/openapi_server/models/ impl_flask/openapi_server/models/

# Activating conda environment (python36)

    cd /Users/mana/manaDev/MyPHR_API
    conda activate python36

