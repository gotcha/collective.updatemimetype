=========================
collective.updatemimetype
=========================

This Plone add-on can be used to update broken mimetypes of Blob fields.

When a file or an image is uploaded to a Blob field, its mimetype is computed
based on information from the ``mimetypes_registry``.

If that registry misses some information, the computed mimetype can be wrong
or too general.

For instance, prior to version 2.0.7 of ``Products.MimetypeRegistry``, 
the default ``mimetypes_registry`` of a Plone portal did not
know of OpenXML mimetypes. Those files would get ``application/zip``
mimetype instead of their proper mimetypes.

As computation of mimetype happens only at load time, upgrading
``Products.MimetypeRegistry`` is not enough to fix broken mimetypes.

The function ``collective.updatemimetype.migrate`` walks over content, looks
for blob fields that would get different mimetype if they would be uploaded again,
and updates those field mimetypes.
It can be called from a GenericSetup upgrade step with::

    from collective.updatemimetype import migrate

    migrate(portal)

.. CAUTION::
    The update can demand a lot of memory and take a long time if your portal holds
    a lot of content.

If you want to limit migration to specific content items, you can pass a ``query``
argument to the ``migrate`` function. For instance, while the code above updates both ``File``
and ``Image`` content items of a default Plone site, the code below would
only update ``File`` content items::

    from collective.updatemimetype import migrate

    catalog_query = {'portal_type': 'File'}

    migrate(portal, catalog_query)


There is also a view registered on the portal. Call it with::

    http://my_domain/my_portal/updatemimetype

The view can also be called with a ``query`` parameter. To limit update to
``File`` items, call the view with::

    http://my_domain/my_portal/updatemimetype?query.portal_type:record:string=File

