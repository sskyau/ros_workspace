/*
 * Interface wrapper code.
 *
 * Generated by SIP 4.19.7
 */

#include "sipAPIlibrviz_sip.h"

#line 7 "config.sip"
#define ROS_PACKAGE_NAME "rviz"
#include <rviz/config.h>
#line 45 "config.sip"
#define ROS_PACKAGE_NAME "rviz"
#include <rviz/config.h>
#line 16 "/home/skyau/ros_workspace/build/rviz/sip/rviz_sip/siplibrviz_siprvizConfigMapIterator.cpp"

#line 7 "config.sip"
#define ROS_PACKAGE_NAME "rviz"
#include <rviz/config.h>
#line 21 "/home/skyau/ros_workspace/build/rviz/sip/rviz_sip/siplibrviz_siprvizConfigMapIterator.cpp"
#line 27 "/usr/share/sip/PyQt5/QtCore/qstring.sip"
#include <qstring.h>
#line 24 "/home/skyau/ros_workspace/build/rviz/sip/rviz_sip/siplibrviz_siprvizConfigMapIterator.cpp"


extern "C" {static PyObject *meth_rviz_Config_MapIterator_advance(PyObject *, PyObject *);}
static PyObject *meth_rviz_Config_MapIterator_advance(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::rviz::Config::MapIterator *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_rviz_Config_MapIterator, &sipCpp))
        {
            sipCpp->advance();

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_MapIterator, sipName_advance, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_rviz_Config_MapIterator_isValid(PyObject *, PyObject *);}
static PyObject *meth_rviz_Config_MapIterator_isValid(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::rviz::Config::MapIterator *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_rviz_Config_MapIterator, &sipCpp))
        {
            bool sipRes;

            sipRes = sipCpp->isValid();

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_MapIterator, sipName_isValid, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_rviz_Config_MapIterator_start(PyObject *, PyObject *);}
static PyObject *meth_rviz_Config_MapIterator_start(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::rviz::Config::MapIterator *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_rviz_Config_MapIterator, &sipCpp))
        {
            sipCpp->start();

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_MapIterator, sipName_start, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_rviz_Config_MapIterator_currentKey(PyObject *, PyObject *);}
static PyObject *meth_rviz_Config_MapIterator_currentKey(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::rviz::Config::MapIterator *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_rviz_Config_MapIterator, &sipCpp))
        {
             ::QString*sipRes;

            sipRes = new  ::QString(sipCpp->currentKey());

            return sipConvertFromNewType(sipRes,sipType_QString,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_MapIterator, sipName_currentKey, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_rviz_Config_MapIterator_currentChild(PyObject *, PyObject *);}
static PyObject *meth_rviz_Config_MapIterator_currentChild(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
         ::rviz::Config::MapIterator *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_rviz_Config_MapIterator, &sipCpp))
        {
             ::rviz::Config*sipRes;

            sipRes = new  ::rviz::Config(sipCpp->currentChild());

            return sipConvertFromNewType(sipRes,sipType_rviz_Config,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_MapIterator, sipName_currentChild, NULL);

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_rviz_Config_MapIterator(void *, int);}
static void release_rviz_Config_MapIterator(void *sipCppV, int)
{
    delete reinterpret_cast< ::rviz::Config::MapIterator *>(sipCppV);
}


extern "C" {static void dealloc_rviz_Config_MapIterator(sipSimpleWrapper *);}
static void dealloc_rviz_Config_MapIterator(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_rviz_Config_MapIterator(sipGetAddress(sipSelf), 0);
    }
}


static PyMethodDef methods_rviz_Config_MapIterator[] = {
    {SIP_MLNAME_CAST(sipName_advance), meth_rviz_Config_MapIterator_advance, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_currentChild), meth_rviz_Config_MapIterator_currentChild, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_currentKey), meth_rviz_Config_MapIterator_currentKey, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_isValid), meth_rviz_Config_MapIterator_isValid, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_start), meth_rviz_Config_MapIterator_start, METH_VARARGS, NULL}
};


static pyqt5ClassPluginDef plugin_rviz_Config_MapIterator = {
    0,
    0,
    0,
    0
};


sipClassTypeDef sipTypeDef_librviz_sip_rviz_Config_MapIterator = {
    {
        -1,
        0,
        0,
        SIP_TYPE_SUPER_INIT|SIP_TYPE_CLASS,
        sipNameNr_rviz__Config__MapIterator,
        {0},
        &plugin_rviz_Config_MapIterator
    },
    {
        sipNameNr_MapIterator,
        {2, 255, 0},
        5, methods_rviz_Config_MapIterator,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    0,
    -1,
    sipNameNr_sip_simplewrapper,
    0,
    0,
    0,
    0,
    0,
#if PY_MAJOR_VERSION >= 3
    0,
    0,
#else
    0,
    0,
    0,
    0,
#endif
    dealloc_rviz_Config_MapIterator,
    0,
    0,
    0,
    release_rviz_Config_MapIterator,
    0,
    0,
    0,
    0,
    0,
    0,
    0
};