package logger

import (
	"fmt"
	"io"
	"os"
	"runtime"
	"strings"
	"time"
)

type LogLevel int

const (
	DEBUG LogLevel = iota
	INFO
	WARN
	ERROR
	FATAL
)

func (l LogLevel) String() string {
	switch l {
	case DEBUG:
		return "DEBUG"
	case INFO:
		return "INFO"
	case WARN:
		return "WARN"
	case ERROR:
		return "ERROR"
	case FATAL:
		return "FATAL"
	default:
		return "UNKNOWN"
	}
}

type Logger struct {
	level      LogLevel
	output     io.Writer
	prefix     string
	enableFile bool
	fileOutput *os.File
	formatter  Formatter
}

type Config struct {
	Level      LogLevel
	Output     io.Writer
	Prefix     string
	EnableFile bool
	FilePath   string
	Formatter  Formatter
}

var defaultLogger *Logger

func init() {
	defaultLogger = New(Config{
		Level:     INFO,
		Output:    os.Stdout,
		Prefix:    "[SWECCHI]",
		Formatter: &ColorFormatter{},
	})
}

func New(config Config) *Logger {
	logger := &Logger{
		level:     config.Level,
		output:    config.Output,
		prefix:    config.Prefix,
		formatter: config.Formatter,
	}

	if config.EnableFile && config.FilePath != "" {
		file, err := os.OpenFile(config.FilePath, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
		if err == nil {
			logger.fileOutput = file
			logger.enableFile = true
		}
	}

	if logger.formatter == nil {
		logger.formatter = &DefaultFormatter{}
	}

	return logger
}

func (l *Logger) SetLevel(level LogLevel) {
	l.level = level
}

func (l *Logger) SetOutput(output io.Writer) {
	l.output = output
}

func (l *Logger) log(level LogLevel, args ...interface{}) {
	if level < l.level {
		return
	}

	_, file, line, _ := runtime.Caller(2)
	fileName := getFileName(file)

	message := l.formatter.Format(LogEntry{
		Time:    time.Now(),
		Level:   level,
		Message: fmt.Sprint(args...),
		File:    fileName,
		Line:    line,
		Prefix:  l.prefix,
	})

	if l.output != nil {
		fmt.Fprint(l.output, message)
	}

	if l.enableFile && l.fileOutput != nil {
		plainFormatter := &DefaultFormatter{}
		plainMessage := plainFormatter.Format(LogEntry{
			Time:    time.Now(),
			Level:   level,
			Message: fmt.Sprint(args...),
			File:    fileName,
			Line:    line,
			Prefix:  l.prefix,
		})
		fmt.Fprint(l.fileOutput, plainMessage)
	}

	if level == FATAL {
		os.Exit(1)
	}
}

func (l *Logger) logf(level LogLevel, format string, args ...interface{}) {
	if level < l.level {
		return
	}

	_, file, line, _ := runtime.Caller(2)
	fileName := getFileName(file)

	message := l.formatter.Format(LogEntry{
		Time:    time.Now(),
		Level:   level,
		Message: fmt.Sprintf(format, args...),
		File:    fileName,
		Line:    line,
		Prefix:  l.prefix,
	})

	if l.output != nil {
		fmt.Fprint(l.output, message)
	}

	if l.enableFile && l.fileOutput != nil {
		plainFormatter := &DefaultFormatter{}
		plainMessage := plainFormatter.Format(LogEntry{
			Time:    time.Now(),
			Level:   level,
			Message: fmt.Sprintf(format, args...),
			File:    fileName,
			Line:    line,
			Prefix:  l.prefix,
		})
		fmt.Fprint(l.fileOutput, plainMessage)
	}

	if level == FATAL {
		os.Exit(1)
	}
}

func (l *Logger) Debug(args ...interface{}) {
	l.log(DEBUG, args...)
}

func (l *Logger) Debugf(format string, args ...interface{}) {
	l.logf(DEBUG, format, args...)
}

func (l *Logger) Info(args ...interface{}) {
	l.log(INFO, args...)
}

func (l *Logger) Infof(format string, args ...interface{}) {
	l.logf(INFO, format, args...)
}

func (l *Logger) Warn(args ...interface{}) {
	l.log(WARN, args...)
}

func (l *Logger) Warnf(format string, args ...interface{}) {
	l.logf(WARN, format, args...)
}

func (l *Logger) Error(args ...interface{}) {
	l.log(ERROR, args...)
}

func (l *Logger) Errorf(format string, args ...interface{}) {
	l.logf(ERROR, format, args...)
}

func (l *Logger) Fatal(args ...interface{}) {
	l.log(FATAL, args...)
}

func (l *Logger) Fatalf(format string, args ...interface{}) {
	l.logf(FATAL, format, args...)
}

func (l *Logger) Close() error {
	if l.fileOutput != nil {
		return l.fileOutput.Close()
	}
	return nil
}

func Debug(args ...interface{}) {
	defaultLogger.Debug(args...)
}

func Debugf(format string, args ...interface{}) {
	defaultLogger.Debugf(format, args...)
}

func Info(args ...interface{}) {
	defaultLogger.Info(args...)
}

func Infof(format string, args ...interface{}) {
	defaultLogger.Infof(format, args...)
}

func Warn(args ...interface{}) {
	defaultLogger.Warn(args...)
}

func Warnf(format string, args ...interface{}) {
	defaultLogger.Warnf(format, args...)
}

func Error(args ...interface{}) {
	defaultLogger.Error(args...)
}

func Errorf(format string, args ...interface{}) {
	defaultLogger.Errorf(format, args...)
}

func Fatal(args ...interface{}) {
	defaultLogger.Fatal(args...)
}

func Fatalf(format string, args ...interface{}) {
	defaultLogger.Fatalf(format, args...)
}

func SetLevel(level LogLevel) {
	defaultLogger.SetLevel(level)
}

func SetOutput(output io.Writer) {
	defaultLogger.SetOutput(output)
}

func getFileName(file string) string {
	parts := strings.Split(file, "/")
	if len(parts) > 0 {
		return parts[len(parts)-1]
	}
	return file
}
