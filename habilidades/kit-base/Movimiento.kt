package ui

import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.spring
import androidx.compose.ui.unit.IntOffset
import androidx.compose.animation.core.FiniteAnimationSpec

/**
 * Movimiento con nombre, para no inventarse curvas en cada pantalla.
 *
 * Pertenece al kit base: copiar tal cual. Las tres curvas cubren el 99 % de los casos; si
 * alguna vez hace falta una cuarta, es que el diseño está haciendo algo raro.
 *
 * Referencia: Material 3 Expressive, esquema *expressive* — sobrepasa ligeramente el destino y
 * vuelve. Se reserva para momentos protagonistas (elegir una pestaña, cambiar de estado), no
 * para todo.
 */
object Movimiento {

    /** Lo que se toca y responde: pestañas, chips, botones. Rebote perceptible. */
    fun <T> muelle(): FiniteAnimationSpec<T> = spring(
        dampingRatio = Spring.DampingRatioMediumBouncy,
        stiffness = Spring.StiffnessMediumLow,
    )

    /** Cambios de estado: aparece un aviso, cambia un color. Rebote mínimo. */
    fun <T> suave(): FiniteAnimationSpec<T> = spring(
        dampingRatio = Spring.DampingRatioNoBouncy,
        stiffness = Spring.StiffnessMedium,
    )

    /** Lo inmediato: un visto que se dibuja, un contador. Nada de esperas. */
    fun <T> seco(): FiniteAnimationSpec<T> = spring(
        dampingRatio = Spring.DampingRatioNoBouncy,
        stiffness = Spring.StiffnessHigh,
    )

    /** Desplazamientos espaciales (hojas, píldoras que se mueven). */
    fun desplazamiento(): FiniteAnimationSpec<IntOffset> = spring(
        dampingRatio = Spring.DampingRatioLowBouncy,
        stiffness = Spring.StiffnessMediumLow,
        visibilityThreshold = IntOffset.VisibilityThreshold,
    )

    // Duraciones de referencia, por si se usa animación por tiempo en lugar de muelle:
    const val INMEDIATO_MS = 120   // 50–150
    const val ESPACIAL_MS = 280    // 200–400
    // Nada de 600 ms: eso no es elegancia, es lentitud.
}
