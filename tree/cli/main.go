package main

import (
	"os"
	"swecchi/pkg/logger"
)

func init() {
	logger.Info("app cli init")
}

func main() {
	os.Exit(0)
}
