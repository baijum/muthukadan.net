---
layout: single
title: Why Should You Support Service Binding Specification for Kubernetes?
date: 2021-07-18
categories: kubernetes binding
---

[Service Binding Specification][spec] for Kubernetes standardizes exposing
backing service secrets to applications.  A _backing service_ is any process
that the application consumes over the network as part of its regular operation.
Examples include datastores (such as MySQL or MongoDB), caching servers (such as
Memcached), and stream processing systems (such as Kafka).  If you are a backing
service provider, this article gives you all the information required to
evaluate Service Binding Specification for Kubernetes.  There is an expository
commentary on the spec related to backing service integration.  Finally, the
article has curated a list of frequently asked questions with answers.

The spec [introduction][spec-intro] presents a good summary of the importance of
the specification.  The key benefit for supporting the spec for a backing
service is that the Secret resource will be collected and exposed to
applications consistently and predictably.

Few facts about the spec:

- The spec is a collective effort of a community working with Kuberentes.
- Contributions from many organizations including VMware, IBM, and Red Hat.
- The spec is matured and GA release will happen soon
- The [Provisioned Service][provisioned-service] part for backing service is stable and ready for adoption

## Projects with Support for Service Binding

Currently the Kuberentes ecosystem is getting ready for the spec adoption.  Here
is a list of projects with support for Service Binding:

- [https://camel.apache.org/camel-k/latest/traits/service-binding.html](https://camel.apache.org/camel-k/latest/traits/service-binding.html)
- [https://github.com/spring-cloud/spring-cloud-bindings](https://github.com/spring-cloud/spring-cloud-bindings)
- [https://github.com/nodeshift/kube-service-bindings](https://github.com/nodeshift/kube-service-bindings)
- [https://pypi.org/project/pyservicebinding/](https://pypi.org/project/pyservicebinding/)
- [https://github.com/baijum/servicebinding](https://github.com/baijum/servicebinding)
- [https://quarkus.io/guides/deploying-to-kubernetes#service-binding](https://quarkus.io/guides/deploying-to-kubernetes#service-binding)
- [https://paketo.io/docs/reference/configuration/#bindings](https://paketo.io/docs/reference/configuration/#bindings)

## Operator Implementations

1. [Red Hat implementation](https://github.com/redhat-developer/service-binding-operator)
2. [VMware implementation](https://github.com/vmware-labs/service-bindings)
3. [KubePreset](https://kubepreset.dev) - A side-project of [Baiju Muthukadan](https://twitter.com/baijum)
4. [Service Binding Controller](https://github.com/k8s-service-bindings/service-binding-controller) - Reference implementation

## Provisioned Service

[Provisioned Service][provisioned-service] is the key abstraction used in the
spec to define a backing service.  The spec consider Provisioned Service as a
duck type with a definition like this:

> Any type that meets the contract defined in a specification, without being an
> instance of a specific concrete type.  For example, for specification that
> requires a given key on `status`, any resource that has that key on its
> `status` regardless of its kind would be considered a duck type of the
> specification.

The Provisioned Service section starts like this:

> A Provisioned Service resource **MUST** define a `.status.binding` which is a
> `LocalObjectReference`-able (containing a single field `name`) to a `Secret`.

The
[LocalObjectReference](https://pkg.go.dev/k8s.io/api/core/v1#LocalObjectReference)
is a type with `name` field.  The name should point to a Secret resource with
data entries for the application to connect to the backing service.  Service
Binding recociler will project the Secret values in to the application as
defined in the [Application
Projection](https://github.com/k8s-service-bindings/spec#application-projection)
section of the spec.  As you can see the sentence has the key word **MUST** in
full capital and bold, that indicates this is a mandatory requirement to comform
to the spec.

This is the next mandatory requirement:

> The `Secret` **MUST** be in the same namespace as the resource.

If the provisioned service and applications are in different namespaces, users
may consider using [Provisioned Service Syncer
Operator](https://github.com/kubepreset/provisioned-service-syncer) to sync the
Secret resource across namespace.

The next sentence is not a mandate, but a recommendation:

> The `Secret` data **SHOULD** contain a `type` entry with a value that
> identifies the abstract classification of the binding.

This is a recommendation to the provisioned service, but when it comes to the
Application Projection, it becomes a mandatory requirement as part of the
projected bindings data.  Even if the provisioned service provides a value for
`type`, it is possible to override the value from the `ServiceBinding` resource.

There is no standardization on the value for `type`, but you can see some good
examples used in the [Spring Cloud
Bindings](https://github.com/spring-cloud/spring-cloud-bindings#auto-configurations).
Few examples:

- cassandra
- couchbase
- db2
- elasticsearch
- kafka
- ldap
- mongodb
- mysql
- neo4j
- oracle
- postgresql
- rabbitmq
- redis
- sqlserver
- vault

Next recommendation:

> The `Secret` type (`.type` verses `.data.type`) **SHOULD** reflect this value
> as `service.binding/{type}`, replacing `{type}` with the `Secret` data type.

This recommendation helps to query Secret resources of particular type using
field-selector.  For example:

    kubectl get secrets --field-selector="type=service.binding/postgresql"

will give the Secret resources of `postgresql` type/

Next recommendation:

> It is **RECOMMENDED** that the `Secret` data also contain a `provider` entry
> with a value that identifies the provider of the binding.

The `provider` field helps to narrow down the tye further in the application.
The provider field could be used where there are different providers for the
same Provisioned Service type.  For example, if the type is `mysql`, the
provider value could be `mariadb`, `oracle`, `bitnami`, `aws-rds`, etc.  When
the application is reading the binding values, if necessary, the application
could consider `type` and `provider` as a composite key to avoid ambiguity.

Next recommendation:

> The `Secret` data **MAY** contain any other entry.

Apart from the `type` and `provider` entries, the Secret data can include
`username`, `password`, `host`, `port` etc.

Next recommendation:

> To facilitate discoverability, it is **RECOMMENDED** that a
> `CustomResourceDefinition` exposing a Provisioned Service add
> `service.binding/provisioned-service: "true"` as a label.

This helps to find all the Provisioned Service custom resouces.  For example:

    kubectl get customresourcedefinitions.apiextensions.k8s.io -l "service.binding/provisioned-service=true"

Next there is a side note:

> Note: While the Provisioned Service referenced `Secret` data should contain a
> `type` entry, the `type` must be defined before it is projected into an
> application workload.  This allows a mapping to enrich an existing secret.

This is already discussed earlier.

Next recommendation:

> Extensions and implementations **MAY** define additional mechanisms to consume
> a Provisioned Service that does not conform to the duck type.

This recommendation is added to unblock any extensions or implementations with
special requirements.

### Well-known Secret Entries

This is the mandatory requirement about [well-known Secret
entries](https://github.com/k8s-service-bindings/spec#well-known-secret-entries).
Thought, it is acceptable not to include any of these entries in the Secret
resource.

> Other than the recommended `type` and `provider` entries, there are no other
> reserved `Secret` entries.  In the interests of consistency, if a `Secret`
> includes any of the following entry names, the entry value **MUST** meet the
> specified requirements:

If the Provisioned Service doesn't include any of the following entry names, no
need to follow the given requirements.

> | Name | Requirements
> | ---- | ------------
> | `host` | A DNS-resolvable host name or IP address
> | `port` | A valid port number
> | `uri` | A valid URI as defined by [RFC3986](https://tools.ietf.org/html/rfc3986)
> | `username` | A string-based username credential
> | `password` | A string-based password credential
> | `certificates` | A collection of PEM-encoded X.509 certificates, representing a certificate chain used in mTLS client authentication
> | `private-key` | A PEM-encoded private key used in mTLS client authentication

For Go based operators, you may consider using
[github.com/kubepreset/pkg/secret](https://github.com/kubepreset/pkg/blob/main/secret/wellknown.go)
package to validate these entries.

> `Secret` entries that do not meet these requirements **MUST** use different entry names.

If there is any entry that doesn't follow the given requirement, you can choose
different names.  For example, if there is a URI-like string but not a valid
one, as per RFC-3986, use another name (e.g., "custom-uri").

### Considerations for Role-Based Access Control (RBAC)

The spec has support for Role-Based Access Control (RBAC).  Since the service
binding reconciler needs permission to read Provisioned Service resources, there
is a mandate about [RBAC][rbac] like this:

> If a service binding reconciler implementation is using Role-Based Access
> Control (RBAC) it **MUST** define an [aggregated `ClusterRole`][acr] with a
> label selector matching the label `service.binding/controller=true`.

So, there must be a `ClusterRole` configured in the Kubernetes cluster something
like this:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: ...
aggregationRule:
  clusterRoleSelectors:
  - matchLabels:
      service.binding/controller: "true"
rules: [] # The control plane automatically fills in the rules
```

There is a recommendation for backing service about RBAC:

> Cluster operators and CRD authors **SHOULD** opt-in resources to expose
> provisioned services by defining a `ClusterRole` with a label matching
> `service.binding/controller=true`, the `get`, `list`, and `watch` verbs
> **MUST** be granted.

As a backing service author, you can offer a `ClusterRole` with that same label
(`service.binding/controller=true`) and the verbs (`get`, `list`, and `watch`)
listed in the rules.  Here is an example `ClusterRole`:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kubepostgres-service-bindings
  labels:
    service.binding/controller: "true" # matches the aggregation rule selector
rules:
- apiGroups:
  - kubepostgres.dev
  resources:
  - databases
  verbs:
  - get
  - list
  - watch
```

In the above example, the API group for the backing service CRD is
`kubepostgres.dev` and the resource name (plural form) is `databases`.  You can
change those values as per your Provisioned Service.  While your operator is
getting installed, make sure this cluster role is also installed.  For example,
if you us Helm charts, you can add the above `ClusterRole` configuration into a
file inside the template directory (e.g., `templates/rbac.yaml`).

## Frequently Asked Questions

### Is it possible to use separate namespaces for Provisioned Services and applications?

Current spec has a strong recommendation to restrict service binding to
provisioned service within the same namespace.

> Restricting service binding to resources within the same namespace is strongly **RECOMMENDED**.

(_From [2nd
paragraph](https://github.com/k8s-service-bindings/spec#service-binding) of
Service Binding section_)

If your provisioned service and applications are in different namespaces, you
may consider using [Provisioned Service Syncer
Operator](https://github.com/kubepreset/provisioned-service-syncer) to sync the
Secret resource across namespace.

### Is it okay to replace the Secret resource name when there is a change in any of the entries?

Yes, it is a good practice to update `.status.binding.name` field value with the
new name of the Secret resource.  After the update, remove the old Secret
resource from the cluster.  That should trigger Service Binding reconciliation
and, in turn, update the projected bindings.  That's the advantage of [level
triggering and reconciliation][level triggering] in Kubernetes!

[spec]: https://github.com/k8s-service-bindings/spec#provisioned-service
[provisioned-service]: https://github.com/k8s-service-bindings/spec#provisioned-service
[spec-intro]: https://github.com/k8s-service-bindings/spec#service-binding-specification-for-kubernetes
[rbac]: https://github.com/k8s-service-bindings/spec#role-based-access-control-rbac
[acr]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles
[level triggering]: https://hackernoon.com/level-triggering-and-reconciliation-in-kubernetes-1f17fe30333d
