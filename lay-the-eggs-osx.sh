rm etc/rpm.egg
rm etc/rpm.egg.asc

CWD=$(pwd)

if [[ -f "/etc/insights-client/rpm.egg" ]]; then
  rm /etc/insights-client/rpm.egg
fi

if [[ -z $1 ]]; then
  if [[ -d "../insights-core" ]]; then
    cd ../insights-core
  else
    echo "../insights-core not found. Please specify a directory where the insights-core repo is located"
    exit
  fi
else
  if [[ -d "$1" ]]; then
    cd $1
  else
    echo "Please specify a valid directory."
    exit
  fi
fi

./build_client_egg.sh
mv insights.zip /etc/insights-client/rpm.egg
exit