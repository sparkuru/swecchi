package main

import (
	"os"
	"swecchi/pkg/logger"
)

func tmp_logger() {
	tmplogger := logger.New(logger.Config{
		Level:      logger.DEBUG,
		Output:     os.Stdout,
		Prefix:     "[TEST]",
		EnableFile: true,
		FilePath:   "logs/test.log",
		Formatter:  &logger.JSONFormatter{},
	})

	tmplogger.Info("test")
	tmplogger.Debugf("test %s", "debug")
	tmplogger.Errorf("test %s", "error")
	tmplogger.Warnf("test %s", "warn")
	tmplogger.Fatalf("test %s", "fatal")

	defer tmplogger.Close()
}

func main() {
	tmp_logger()
}
