{{/* Generate full name */}}
{{- define "fastapi.fullname" -}}
{{- printf "%s-fastapi" .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/* Common labels */}}
{{- define "fastapi.labels" -}}
app.kubernetes.io/name: {{ include "fastapi.fullname" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}