python_test() {
  if python3 testing.py 2>&1 = 0; then
    echo success!
  else
    exit 1
  fi
}

python_test

cython main.py
echo 'exit code' $?
